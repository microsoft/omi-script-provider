# OMI Python Script Provider


### Additional Resources

- [Script Provider Getting Started Guide](/doc/ScriptProviderGettingStarted.pdf)

## How to build

### Dependencies to build OMI Python Script Provider:

Before you build OMI Python Script Provider, you should check [OMI_Build_Dependencies](https://github.com/Microsoft/Build-omi#dependencies-to-build-a-native-package), then you can build the provider as following:

- Install python and python-devel
  - Redhat/CentOS: 
    ```
    sudo yum update
    sudo yum install python27 python27-devel
    ```
  - Debian/Ubuntu OS: 
    ```
    sudo apt-get update
    sudo apt-get install python2.7 python2.7-dev 
    ```
    Note: If you use old OS version like Ubuntu 12.04 or Ubuntu 14.04, you might need to run command:`sudo add-apt-repository ppa:fkrull/deadsnakes` to get python to be installed.

### To clone the repository to build OMI Python Script Provider, issue the following commands:
```
git clone --recursive https://github.com/Microsoft/Build-omi-script-provider
cd Build-omi-script-provider/omi/Unix
./configure --dev
make -j
make install
cd ../../scriptprovider
make
sudo make install
```

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
