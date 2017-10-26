// Copyright (c) Microsoft Corporation.  All rights reserved.
// Licensed under the MIT license.
#include "mi_schema.hpp"


#include <algorithm>
#include <cassert>
#include <cctype>
#include "shared_protocol.hpp"


namespace
{


template<typename CHAR_t>
inline int
compare_case_insensitive (
    CHAR_t const* pLHS,
    CHAR_t const* pRHS)
{
    for (; *pLHS || *pRHS; ++pLHS, ++pRHS)
    {
        CHAR_t l = tolower (*pLHS);
        CHAR_t r = tolower (*pRHS);
        if (l != r)
        {
            return l < r ? -1 : 1;
        }
    }
    return 0;
}


bool
classDeclSort (
    scx::MI_ClassDecl::Ptr pLeft,
    scx::MI_ClassDecl::Ptr pRight)
{
    return 0 > compare_case_insensitive (
        pLeft->getName ()->getValue ().c_str (),
        pRight->getName ()->getValue ().c_str ());
                                         
}


scx::MI_ClassDecl::ConstPtr
findClassDecl (
    std::vector<scx::MI_ClassDecl::Ptr> const& classDecls,
    scx::MI_Value<MI_STRING>::ConstPtr const& pName)
{
    if (pName)
    {
        typedef std::vector<scx::MI_ClassDecl::Ptr>::size_type index_t;
        index_t left = 0;
        index_t right = classDecls.size ();
        while (left < right)
        {
            index_t mid = (left + right) / 2;
            int const ret = compare_case_insensitive (
                pName->getValue ().c_str (),
                classDecls[mid]->getName ()->getValue ().c_str ());
            if (ret < 0)
            {
                right = mid;
            }
            else if (0 < ret)
            {
                left = mid + 1;
            }
            else
            {
                return scx::MI_ClassDecl::Ptr (classDecls[mid]);
            }
        }
    }
    return scx::MI_ClassDecl::Ptr ();
}


template<typename OBJECT>
struct Finder
{
    /*ctor*/ Finder (scx::MI_Value<MI_STRING>::type_t const& name)
        : m_Name (name)
    {
        // empty
    }

    bool operator () (typename OBJECT::ConstPtr const& pObject)
    {
        return m_Name == pObject->getName ()->getValue ();
    }

    scx::MI_Value<MI_STRING>::type_t const& m_Name;
};


} // namespace (unnamed)


namespace scx
{


#if (0)
#define PRINT_QD (PRINT_BOOKENDS)
#else
#define PRINT_QD (0)
#endif

#if (PRINT_QD)
#define QD_BOOKEND(x) SCX_BOOKEND (x)
#else
#define QD_BOOKEND(x)
#endif

/*ctor*/
MI_QualifierDecl::MI_QualifierDecl (
    MI_Value<MI_STRING>::ConstPtr const& pName,
    MI_Value<MI_UINT32>::ConstPtr const& pType,
    MI_Value<MI_UINT32>::ConstPtr const& pScope,
    MI_Value<MI_UINT32>::ConstPtr const& pFlavor,
    MI_ValueBase::ConstPtr const& pValue)
    : m_pName (pName)
    , m_pType (pType)
    , m_pScope (pScope)
    , m_pFlavor (pFlavor)
    , m_pValue (pValue)
{
    QD_BOOKEND ("MI_QualifierDecl::ctor");
    assert (pName);
    assert (pType);
    assert (pScope);
    assert (pFlavor);
    assert (NULL == pValue.get () || pValue->getType () == pType->getValue ());
}


/*dtor*/
MI_QualifierDecl::~MI_QualifierDecl ()
{
    QD_BOOKEND ("MI_QualiferDecl::dtor");
}


MI_Value<MI_STRING>::ConstPtr const&
MI_QualifierDecl::getName () const
{
    return m_pName;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_QualifierDecl::getType () const
{
    return m_pType;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_QualifierDecl::getScope () const
{
    return m_pScope;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_QualifierDecl::getFlavor () const
{
    return m_pFlavor;
}


MI_ValueBase::ConstPtr const&
MI_QualifierDecl::getValue () const
{
    return m_pValue;
}


int
MI_QualifierDecl::send (
    socket_wrapper& sock) const
{
    int rval = socket_wrapper::SUCCESS;
    rval = m_pName->send (sock);
    if (socket_wrapper::SUCCESS == rval)
    {
        protocol::data_type_t const type = static_cast<protocol::data_type_t>(
            m_pType->getValue () | (m_pValue ? 0 : protocol::MI_NULL_FLAG));
        rval = protocol::send (type, sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        rval = m_pScope->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        rval = m_pFlavor->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval &&
        m_pValue)
    {
        rval = m_pValue->send (sock);
    }
    return rval;
}


#if (0)
#define PRINT_Q (PRINT_BOOKENDS)
#else
#define PRINT_Q (0)
#endif

#if (PRINT_Q)
#define Q_BOOKEND(x) SCX_BOOKEND (x)
#else
#define Q_BOOKEND(x)
#endif

/*ctor*/
MI_Qualifier::MI_Qualifier (
    MI_Value<MI_STRING>::ConstPtr const& pName,
    MI_Value<MI_UINT32>::ConstPtr const& pType,
    MI_Value<MI_UINT32>::ConstPtr const& pFlavor,
    MI_ValueBase::ConstPtr const& pValue)
    : m_pName (pName)
    , m_pType (pType)
    , m_pFlavor (pFlavor)
    , m_pValue (pValue)
{
    Q_BOOKEND ("MI_Qualifier::ctor");
    assert (pName);
    assert (pType);
    assert (pFlavor);
    assert (NULL == pValue.get () || pValue->getType () == pType->getValue ());
}


/*dtor*/
MI_Qualifier::~MI_Qualifier ()
{
    Q_BOOKEND ("MI_Qualifer::dtor");
    // empty
}


MI_Value<MI_STRING>::ConstPtr const&
MI_Qualifier::getName () const
{
    return m_pName;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_Qualifier::getType () const
{
    return m_pType;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_Qualifier::getFlavor () const
{
    return m_pFlavor;
}


MI_ValueBase::ConstPtr const&
MI_Qualifier::getValue () const
{
    return m_pValue;
}


int
MI_Qualifier::send (
    socket_wrapper& sock) const
{
    int rval = socket_wrapper::SUCCESS;
    rval = m_pName->send (sock);
    if (socket_wrapper::SUCCESS == rval)
    {
        protocol::data_type_t const type = static_cast<protocol::data_type_t>(
            m_pType->getValue () | (m_pValue ? 0 : protocol::MI_NULL_FLAG));
        rval = protocol::send_type (type, sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        rval = m_pFlavor->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval &&
        m_pValue)
    {
        rval = m_pValue->send (sock);
    }
    return rval;
}


#if (0)
#define PRINT_PD (PRINT_BOOKENDS)
#else
#define PRINT_PD (0)
#endif

#if (PRINT_PD)
#define PD_BOOKEND(x) SCX_BOOKEND (x)
#define PD_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define PD_BOOKEND(x)
#define PD_PRINT(x)
#endif

/*ctor*/
MI_ParameterDecl::MI_ParameterDecl (
    MI_Value<MI_UINT32>::ConstPtr const& flags,
    MI_Value<MI_UINT32>::ConstPtr const& code,
    MI_Value<MI_STRING>::ConstPtr const& name,
    MI_Qualifier::ConstPtr const* const ppQualifiersBegin,
    size_t const& qualifiersCount,
    MI_Value<MI_UINT32>::ConstPtr const& type,
    MI_Value<MI_STRING>::ConstPtr const& className)
    : m_pFlags (flags)
    , m_pCode (code)
    , m_pName (name)
    , m_Qualifiers (ppQualifiersBegin, ppQualifiersBegin + qualifiersCount)
    , m_pType (type)
    , m_pClassName (className)
{
    PD_BOOKEND ("MI_ParameterDecl::ctor");
}


/*dtor*/
MI_ParameterDecl::~MI_ParameterDecl ()
{
    PD_BOOKEND ("MI_ParameterDecl::dtor");
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_ParameterDecl::getFlags () const
{
    return m_pFlags;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_ParameterDecl::getCode () const
{
    return m_pCode;
}


MI_Value<MI_STRING>::ConstPtr const&
MI_ParameterDecl::getName () const
{
    return m_pName;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_ParameterDecl::getType () const
{
    return m_pType;
}


MI_Value<MI_STRING>::ConstPtr const&
MI_ParameterDecl::getClassName () const
{
    return m_pClassName;
}


int
MI_ParameterDecl::send (
    socket_wrapper& sock) const
{
    PD_BOOKEND ("MI_ParameterDecl::send");
    int rval = socket_wrapper::SUCCESS;
#if (PRINT_PD)
    std::ostringstream strm;
    strm << "send flags: " << m_pFlags->getValue ();
    PD_PRINT (strm.str ());
    strm.clear ();
    strm.str ("");
#endif
    rval = m_pFlags->send (sock);
    if (socket_wrapper::SUCCESS == rval)
    {
#if (PRINT_PD)
        strm << "send code: " << m_pCode->getValue ();
        PD_PRINT (strm.str ());
        strm.clear ();
        strm.str ("");
#endif
        rval = m_pCode->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
#if (PRINT_PD)
        strm << "send name: \"" << m_pName->getValue () << "\"";
        PD_PRINT (strm.str ());
        strm.clear ();
        strm.str ("");
#endif
        rval = m_pName->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
#if (PRINT_PD)
        PD_BOOKEND ("send qualifiers");
        strm << "send count: " << m_Qualifiers.size ();
        PD_PRINT (strm.str ());
        strm.clear ();
        strm.str ("");
#endif
        rval = protocol::send_item_count (m_Qualifiers.size (), sock);
        for (std::vector<MI_Qualifier::ConstPtr>::const_iterator
                 pos = m_Qualifiers.begin (),
                 endPos = m_Qualifiers.end ();
             socket_wrapper::SUCCESS == rval &&
                 pos != endPos;
             ++pos)
        {
            PD_PRINT ("---- send qualifier");
            rval = (*pos)->send (sock);
        }
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        rval = send_type (sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
#if (PRINT_PD)
        strm << "send classname: ";
        if (m_pClassName)
        {
            strm << "\"" << m_pClassName->getValue () << "\"";
        }
        else
        {
            strm << "NULL";
        }
        PD_PRINT (strm.str ());
        strm.clear ();
        strm.str ("");
#endif
        rval = protocol::send (m_pClassName, sock);
    }
    return rval;
}


int
MI_ParameterDecl::send_type (
    socket_wrapper& sock) const
{
    return protocol::send_type (m_pType->getValue (), sock);
}
    

#if (0)
#define PRINT_PROP (PRINT_BOOKENDS)
#else
#define PRINT_PROP (0)
#endif

#if (PRINT_PROP)
#define PROP_BOOKEND(x) SCX_BOOKEND (x)
#define PROP_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define PROP_BOOKEND(x)
#define PROP_PRINT(x)
#endif

/*ctor*/
MI_PropertyDecl::MI_PropertyDecl (
    MI_Value<MI_UINT32>::ConstPtr const& pFlags,
    MI_Value<MI_UINT32>::ConstPtr const& pCode,
    MI_Value<MI_STRING>::ConstPtr const& pName,
    MI_Qualifier::ConstPtr const* const ppQualifiersBegin,
    size_t const& qualifiersCount,
    MI_Value<MI_UINT32>::ConstPtr const& pType,
    MI_Value<MI_STRING>::ConstPtr const& pClassName,
    MI_Value<MI_STRING>::ConstPtr const& pOrigin,
    MI_Value<MI_STRING>::ConstPtr const& pPropagator,
    MI_ValueBase::ConstPtr const& pValue)
    : MI_ParameterDecl (pFlags, pCode, pName, ppQualifiersBegin,
                        qualifiersCount, pType, pClassName)
    , m_pOrigin (pOrigin)
    , m_pPropagator (pPropagator)
    , m_pValue (pValue)
{
    PROP_BOOKEND ("MI_PropertyDecl::ctor");
    assert (pFlags);
    assert (pCode);
    assert (pName);
    assert (pType);
    assert (pOrigin);
    assert (pPropagator);
    assert (NULL == pValue.get () || pValue->getType () == pType->getValue ());
}


/*dtor*/
MI_PropertyDecl::~MI_PropertyDecl ()
{
    PROP_BOOKEND ("MI_PropertyDecl::dtor");
}


MI_Value<MI_STRING>::ConstPtr const&
MI_PropertyDecl::getOrigin () const
{
    return m_pOrigin;
}


MI_Value<MI_STRING>::ConstPtr const&
MI_PropertyDecl::getPropagator () const
{
    return m_pPropagator;
}


MI_ValueBase::ConstPtr const&
MI_PropertyDecl::getValue () const
{
    return m_pValue;
}


int
MI_PropertyDecl::send (
    socket_wrapper& sock) const
{
    PROP_BOOKEND ("MI_PropertyDecl::send");
    int rval = MI_ParameterDecl::send (sock);
#if (PRINT_PROP)
    std::ostringstream strm;
#endif
    if (socket_wrapper::SUCCESS == rval)
    {
#if (PRINT_PROP)
        strm << "send origin: ";
        if (m_pOrigin)
        {
            strm << "\"" << m_pOrigin->getValue () << "\"";
        }
        else
        {
            strm << "NULL";
        }
        PROP_PRINT (strm.str ());
        strm.str ("");
        strm.clear ();
#endif
        rval = protocol::send (m_pOrigin, sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
#if (PRINT_PROP)
        strm << "send propagator: ";
        if (m_pPropagator)
        {
            strm << "\"" << m_pPropagator->getValue () << "\"";
        }
        else
        {
            strm << "NULL";
        }
        PROP_PRINT (strm.str ());
        strm.str ("");
        strm.clear ();
#endif
        rval = protocol::send (m_pPropagator, sock);
    }
    if (socket_wrapper::SUCCESS == rval &&
        m_pValue)
    {
        PROP_PRINT ("send value");
        rval = m_pValue->send (sock);
    }
    return rval;
}


int
MI_PropertyDecl::send_type (
    socket_wrapper& sock) const
{
    protocol::data_type_t const type = static_cast<protocol::data_type_t>(
        getType ()->getValue () | (m_pValue ? 0 : protocol::MI_NULL_FLAG));
    return protocol::send_type (type, sock);
}


#if (0)
#define PRINT_OBJ (PRINT_BOOKENDS)
#else
#define PRINT_OBJ (0)
#endif

#if (PRINT_OBJ)
#define OBJ_BOOKEND(x) SCX_BOOKEND (x)
#define OBJ_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define OBJ_BOOKEND(x)
#define OBJ_PRINT(x)
#endif

/*ctor*/
MI_ObjectDecl::MI_ObjectDecl (
    MI_Value<MI_UINT32>::ConstPtr const& pFlags,
    MI_Value<MI_UINT32>::ConstPtr const& pCode,
    MI_Value<MI_STRING>::ConstPtr const& pName,
    MI_Qualifier::ConstPtr const* ppQualifiersBegin,
    size_t const& qualifiersCount,
    MI_ParameterDecl::ConstPtr const* ppParametersBegin,
    size_t const& parametersCount)
    : m_pFlags (pFlags)
    , m_pCode (pCode)
    , m_pName (pName)
    , m_Qualifiers (ppQualifiersBegin, ppQualifiersBegin + qualifiersCount)
    , m_Parameters (ppParametersBegin, ppParametersBegin + parametersCount)
{
    OBJ_BOOKEND ("MI_ObjectDecl::ctor");
    assert (pFlags);
    assert (pCode);
    assert (pName);
}


/*dtor*/
MI_ObjectDecl::~MI_ObjectDecl ()
{
    OBJ_BOOKEND ("MI_ObjectDecl::dtor");
}


bool
MI_ObjectDecl::isMethodDecl () const
{
    return false;
}


MI_ParameterDecl::ConstPtr
MI_ObjectDecl::getParameterDecl (
    MI_Value<MI_STRING>::type_t const& parameterName) const
{
    OBJ_BOOKEND ("MI_ObjectDecl::getParameterDecl");
    MI_ParameterDecl::ConstPtr pParameterDecl;
    std::vector<MI_ParameterDecl::ConstPtr>::const_iterator
        parameterDeclPos = std::find_if (
            m_Parameters.begin (), m_Parameters.end (),
            Finder<MI_ParameterDecl> (parameterName));
    if (m_Parameters.end () != parameterDeclPos)
    {
        // correct: the parameter name is part of the MI_ClassDecl
        // clear the return value and return success
        pParameterDecl = *parameterDeclPos;
    }
    return pParameterDecl;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_ObjectDecl::getFlags () const
{
    return m_pFlags;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_ObjectDecl::getCode () const
{
    return m_pCode;
}


MI_Value<MI_STRING>::ConstPtr const&
MI_ObjectDecl::getName () const
{
    return m_pName;
}


int
MI_ObjectDecl::send (
    socket_wrapper& sock) const
{
    OBJ_BOOKEND ("MI_ObjectDecl::send");
    int rval = socket_wrapper::SUCCESS;
    OBJ_PRINT ("send flags");
    rval = m_pFlags->send (sock);
    if (socket_wrapper::SUCCESS == rval)
    {
        OBJ_PRINT ("send code");
        rval = m_pCode->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        OBJ_PRINT ("send name");
        rval = m_pName->send (sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        OBJ_PRINT ("send qualifier count");
        rval = protocol::send_item_count (m_Qualifiers.size (), sock);
        for (std::vector<MI_Qualifier::ConstPtr>::const_iterator
                 pos = m_Qualifiers.begin (),
                 endPos = m_Qualifiers.end ();
             socket_wrapper::SUCCESS == rval &&
                 pos != endPos;
             ++pos)
        {
            OBJ_PRINT ("---- send qualifier");
            rval = (*pos)->send (sock);
        }
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        rval = protocol::send_item_count (m_Parameters.size (), sock);
        OBJ_PRINT ("send parameter count");
        for (std::vector<MI_ParameterDecl::ConstPtr>::const_iterator
                 pos = m_Parameters.begin (),
                 endPos = m_Parameters.end ();
             socket_wrapper::SUCCESS == rval &&
                 pos != endPos;
             ++pos)
        {
            OBJ_PRINT ("---- send parameter");
            rval = (*pos)->send (sock);
        }
    }
    return rval;
}


#if (0)
#define PRINT_METH (PRINT_BOOKENDS)
#else
#define PRINT_METH (0)
#endif

#if (PRINT_METH)
#define METH_BOOKEND(x) SCX_BOOKEND (x)
#define METH_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define METH_BOOKEND(x)
#define METH_PRINT(x)
#endif

/*ctor*/
MI_MethodDecl::MI_MethodDecl (
    MI_Value<MI_UINT32>::ConstPtr const& pFlags,
    MI_Value<MI_UINT32>::ConstPtr const& pCode,
    MI_Value<MI_STRING>::ConstPtr const& pName,
    MI_Qualifier::ConstPtr const* ppQualifiersBegin,
    size_t const& qualifiersCount,
    MI_ParameterDecl::ConstPtr const* ppParametersBegin,
    size_t const& parametersCount,
    MI_Value<MI_UINT32>::ConstPtr const& pReturnType,
    MI_Value<MI_STRING>::ConstPtr const& pOrigin,
    MI_Value<MI_STRING>::ConstPtr const& pPropagator,
    MI_MethodDecl::InvokeFn::ConstPtr const& pInvokeFn)
    : MI_ObjectDecl (pFlags, pCode, pName, ppQualifiersBegin, qualifiersCount,
                     ppParametersBegin, parametersCount)
    , m_pReturnType (pReturnType)
    , m_pOrigin (pOrigin)
    , m_pPropagator (pPropagator)
    , m_pInvokeFn (pInvokeFn)
{
    METH_BOOKEND ("MI_MethodDecl::ctor");
    assert (pFlags);
    assert (pCode);
    assert (pName);
    assert (pReturnType);
    assert (pInvokeFn);
}


/*dtor*/
MI_MethodDecl::~MI_MethodDecl ()
{
    METH_BOOKEND ("MI_MethodDecl::dtor");
}


bool
MI_MethodDecl::isMethodDecl () const
{
    return true;
}


MI_Value<MI_UINT32>::ConstPtr const&
MI_MethodDecl::getReturnType () const
{
    return m_pReturnType;
}


MI_Value<MI_STRING>::ConstPtr const&
MI_MethodDecl::getOrigin () const
{
    return m_pOrigin;
}


MI_Value<MI_STRING>::ConstPtr const&
MI_MethodDecl::getPropagator () const
{
    return m_pPropagator;
}


MI_MethodDecl::InvokeFn::ConstPtr const&
MI_MethodDecl::getInvokeFn () const
{
    return m_pInvokeFn;
}


int
MI_MethodDecl::send (
    socket_wrapper& sock) const
{
    METH_BOOKEND ("MI_MethodDecl::send");
    int rval = MI_ObjectDecl::send (sock);
    if (socket_wrapper::SUCCESS == rval)
    {
        METH_PRINT ("send return type");
        rval = protocol::send_type (
            static_cast<protocol::data_type_t>(
                m_pReturnType->getValue ()), sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        METH_PRINT ("send origin");
        rval = protocol::send (m_pOrigin, sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        METH_PRINT ("send propagator");
        rval = protocol::send (m_pPropagator, sock);
    }
    return rval;
}


void
MI_MethodDecl::Invoke (
    MI_Context::Ptr const& pContext,
    MI_Value<MI_STRING>::Ptr const& pNameSpace,
    MI_Value<MI_STRING>::Ptr const& pClassName,
    MI_Value<MI_STRING>::Ptr const& pMethodName,
    MI_Instance::Ptr const& pInstanceName,
    MI_Instance::Ptr const& pParameters) const
{
    METH_BOOKEND ("MI_MethodDecl::Invoke");
    return m_pInvokeFn->fn (pContext, pNameSpace, pClassName, pMethodName,
                            pInstanceName, pParameters);
}


std::vector<MI_ParameterDecl::ConstPtr>
convert (MI_PropertyDecl::ConstPtr const* begin, size_t const& count)
{
    typedef std::vector<MI_ParameterDecl::ConstPtr> coll_t;
    coll_t coll;
    std::copy (begin, begin + count, std::back_insert_iterator<coll_t> (coll));
    return coll;
}


#if (0)
#define PRINT_CLASS (PRINT_BOOKENDS)
#else
#define PRINT_CLASS (0)
#endif

#if (PRINT_CLASS)
#define CLASS_BOOKEND(x) SCX_BOOKEND (x)
#define CLASS_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define CLASS_BOOKEND(x)
#define CLASS_PRINT(x)
#endif

/*ctor*/
MI_ClassDecl::MI_ClassDecl (
    MI_Value<MI_UINT32>::ConstPtr const& pFlags,
    MI_Value<MI_UINT32>::ConstPtr const& pCode,
    MI_Value<MI_STRING>::ConstPtr const& pName,
    MI_Qualifier::ConstPtr const* ppQualifiersBegin,
    size_t const& qualifiersCount,
    MI_PropertyDecl::ConstPtr const* ppPropertyDeclsBegin,
    size_t const& propertyDeclsCount,
    MI_Value<MI_STRING>::ConstPtr const& pSuperClassName,
    MI_MethodDecl::Ptr const* ppMethodDeclsBegin,
    size_t const& methodDeclsCount,
    MI_FunctionTable::ConstPtr const& pFunctionTable)
    : MI_ObjectDecl (
        pFlags, pCode, pName, ppQualifiersBegin, qualifiersCount,
        (0 < propertyDeclsCount
         ? &(convert (ppPropertyDeclsBegin, propertyDeclsCount)[0])
            : NULL),
        propertyDeclsCount)
    , m_pSuperClassName (pSuperClassName)
    , m_MethodDecls (ppMethodDeclsBegin, ppMethodDeclsBegin + methodDeclsCount)
    , m_pFunctionTable (pFunctionTable)
{
    CLASS_BOOKEND ("MI_ClassDecl::ctor");
    // empty
}


void
MI_ClassDecl::setOwningClassDecl (
    MI_ClassDecl::Ptr const& pOwningClassDecl)
{
    m_pOwningClassDecl = pOwningClassDecl;
}


MI_PropertyDecl::ConstPtr
MI_ClassDecl::getPropertyDecl (
    MI_Value<MI_STRING>::type_t const& propertyName) const
{
    CLASS_BOOKEND ("MI_ClassDecl::getPropertyDecl");
    MI_ParameterDecl::ConstPtr pParameterDecl (getParameterDecl (propertyName));
    return MI_PropertyDecl::ConstPtr (
        static_cast<MI_PropertyDecl const*>(pParameterDecl.get ()));
}


MI_MethodDecl::ConstPtr
MI_ClassDecl::getMethodDecl (
    MI_Value<MI_STRING>::type_t const& methodName) const
{
    CLASS_BOOKEND ("MI_ClassDecl::getMethodDecl");
    MI_MethodDecl::ConstPtr pMethodDecl;
    std::vector<MI_MethodDecl::Ptr>::const_iterator
        methodDeclPos = std::find_if (
            m_MethodDecls.begin (), m_MethodDecls.end (),
            Finder<MI_MethodDecl> (methodName));
    if (m_MethodDecls.end () != methodDeclPos)
    {
        // correct: the property name is part of the MI_ClassDecl
        // clear the return value and return success
        pMethodDecl = *methodDeclPos;
#if (PRINT_CLASS)
        if (NULL == methodDeclPos->get ())
        {
            CLASS_PRINT ("methodDeclPos->get () is NULL");
        }
        else
        {
            CLASS_PRINT ("methodDeclPos->get () is not NULL");
        }
#endif
    }
    return pMethodDecl;
}


/*dtor*/
MI_ClassDecl::~MI_ClassDecl ()
{
    CLASS_BOOKEND ("MI_ClassDecl::dtor");
}


MI_Value<MI_STRING>::ConstPtr const&
MI_ClassDecl::getSuperClassName () const
{
    return m_pSuperClassName;
}


MI_ClassDecl::ConstPtr const&
MI_ClassDecl::getSuperClassDecl () const
{
    return m_pSuperClassDecl;
}


std::vector<MI_MethodDecl::Ptr> const&
MI_ClassDecl::getMethodDecls () const
{
    return m_MethodDecls;
}


MI_SchemaDecl::ConstPtr const&
MI_ClassDecl::getSchemaDecl () const
{
    return m_pSchemaDecl;
}


MI_FunctionTable::ConstPtr const&
MI_ClassDecl::getFunctionTable () const
{
    return m_pFunctionTable;
}


MI_ClassDecl::ConstPtr const&
MI_ClassDecl::getOwningClassDecl () const
{
    return m_pOwningClassDecl;
}


int
MI_ClassDecl::send (
    socket_wrapper& sock) const
{
    CLASS_BOOKEND ("send ClassDecl");
    int rval = MI_ObjectDecl::send (sock);
    if (socket_wrapper::SUCCESS == rval)
    {
        CLASS_PRINT ("send super class name");
        rval = protocol::send (m_pSuperClassName, sock);
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        CLASS_PRINT ("send method decl size");
        rval = protocol::send_item_count (m_MethodDecls.size (), sock);
        for (std::vector<MI_MethodDecl::Ptr>::const_iterator
                 pos = m_MethodDecls.begin (),
                 endPos = m_MethodDecls.end ();
             socket_wrapper::SUCCESS == rval &&
                 pos != endPos;
             ++pos)
        {
            CLASS_PRINT ("... send method decl");
            rval = (*pos)->send (sock);
        }
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        CLASS_PRINT ("send function table");
        if (m_pFunctionTable)
        {
            CLASS_PRINT ("m_pFunctionTable is not NULL");
            rval = protocol::send (protocol::HAS_FUNCTION_TABLE, sock);
        }
        else
        {
            CLASS_PRINT ("m_pFunctionTable is NULL");
            rval = protocol::send (protocol::NO_FUNCTION_TABLE, sock);
        }
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        CLASS_PRINT ("send owning class name");
        MI_Char const* const owningClassName =
            m_pOwningClassDecl ?
                m_pOwningClassDecl->getName ()->getValue ().c_str () : NULL;
        rval = protocol::send (owningClassName, sock);
    }
    return rval;
}


#if (0)
#define PRINT_SCHEMA (PRINT_BOOKENDS)
#else
#define PRINT_SCHEMA (0)
#endif

#if (PRINT_SCHEMA)
#define SCHEMA_BOOKEND(x) SCX_BOOKEND (x)
#define SCHEMA_PRINT(x) SCX_BOOKEND_PRINT (x)
#else
#define SCHEMA_BOOKEND(x)
#define SCHEMA_PRINT(x)
#endif

/*ctor*/
MI_SchemaDecl::MI_SchemaDecl (
    MI_QualifierDecl::ConstPtr const* const ppQualifierDecls,
    size_t const&  qualifierDeclCount,
    MI_ClassDecl::Ptr const* const ppClassDecls,
    size_t const& classDeclCount)
    : m_QualifierDecls (ppQualifierDecls, ppQualifierDecls + qualifierDeclCount)
    , m_ClassDecls (ppClassDecls, ppClassDecls + classDeclCount)
{
    SCHEMA_BOOKEND ("MI_SchemaDecl::ctor");
    // sort the class decls by name
    std::sort (m_ClassDecls.begin (), m_ClassDecls.end (), classDeclSort);
    // loop through all of the class decls to set schema decl members
    for (std::vector<MI_ClassDecl::Ptr>::iterator pos = m_ClassDecls.begin (),
             endPos = m_ClassDecls.end ();
         pos != endPos;
         ++pos)
    {
        (*pos)->m_pSchemaDecl = this;
        for (std::vector<MI_MethodDecl::Ptr>::iterator
                 methodPos = (*pos)->m_MethodDecls.begin (),
                 methodEndPos = (*pos)->m_MethodDecls.end ();
             methodPos != methodEndPos;
             ++methodPos)
        {
            (*methodPos)->m_pSchemaDecl = this;
        }
    }
}


/*dtor*/
MI_SchemaDecl::~MI_SchemaDecl ()
{
    SCHEMA_BOOKEND ("MI_SchemaDecl::dtor");
    // remove the references from the class decls
    for (std::vector<MI_ClassDecl::Ptr>::iterator pos = m_ClassDecls.begin (),
             endPos = m_ClassDecls.end ();
         pos != endPos;
         ++pos)
    {
        (*pos)->m_pSchemaDecl.reset ();
        for (std::vector<MI_MethodDecl::Ptr>::iterator
                 methodPos = (*pos)->m_MethodDecls.begin (),
                 methodEndPos = (*pos)->m_MethodDecls.end ();
             methodPos != methodEndPos;
             ++methodPos)
        {
            (*methodPos)->m_pSchemaDecl.reset ();
        }
    }
}


MI_ClassDecl::ConstPtr
MI_SchemaDecl::getClassDecl (
    MI_Value<MI_STRING>::ConstPtr const& pClassName) const
{
    SCHEMA_BOOKEND ("MI_SchemaDecl::getClassDecl");
    MI_ClassDecl::ConstPtr pClassDecl (
        findClassDecl (m_ClassDecls, pClassName));
    return pClassDecl;
}


int
MI_SchemaDecl::send (
    socket_wrapper& sock) const
{
    SCHEMA_BOOKEND ("MI_SchemaDecl::send");
    int rval = socket_wrapper::SUCCESS;
    if (socket_wrapper::SUCCESS == rval)
    {
        SCHEMA_BOOKEND ("send qualifierDecls");
        rval = protocol::send_item_count (m_QualifierDecls.size (), sock);
        for (std::vector<MI_QualifierDecl::ConstPtr>::const_iterator
                 pos = m_QualifierDecls.begin (),
                 endPos = m_QualifierDecls.end ();
             socket_wrapper::SUCCESS == rval &&
                 pos != endPos;
             ++pos)
        {
            rval = (*pos)->send (sock);
        }
    }
    if (socket_wrapper::SUCCESS == rval)
    {
        SCHEMA_BOOKEND ("send classDecls");
        rval = protocol::send_item_count (m_ClassDecls.size (), sock);
        for (std::vector<MI_ClassDecl::Ptr>::const_iterator
                 pos = m_ClassDecls.begin (),
                 endPos = m_ClassDecls.end ();
             socket_wrapper::SUCCESS == rval &&
                 pos != endPos;
             ++pos)
        {
            rval = (*pos)->send (sock);
        }
    }
    return rval;
}
    

} // namespace scx
