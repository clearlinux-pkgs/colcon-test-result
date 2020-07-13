#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-test-result
Version  : 0.3.8
Release  : 18
URL      : https://files.pythonhosted.org/packages/7c/e5/690583c1bbb2c9958287e64a59014e69766644d900c4c10f4ed855bbc2d6/colcon-test-result-0.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/7c/e5/690583c1bbb2c9958287e64a59014e69766644d900c4c10f4ed855bbc2d6/colcon-test-result-0.3.8.tar.gz
Summary  : Extension for colcon to provide information about the test results.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-test-result-python = %{version}-%{release}
Requires: colcon-test-result-python3 = %{version}-%{release}
Requires: colcon-core
BuildRequires : buildreq-distutils3
BuildRequires : colcon-core

%description
==================

%package python
Summary: python components for the colcon-test-result package.
Group: Default
Requires: colcon-test-result-python3 = %{version}-%{release}

%description python
python components for the colcon-test-result package.


%package python3
Summary: python3 components for the colcon-test-result package.
Group: Default
Requires: python3-core
Provides: pypi(colcon_test_result)
Requires: pypi(colcon_core)

%description python3
python3 components for the colcon-test-result package.


%prep
%setup -q -n colcon-test-result-0.3.8
cd %{_builddir}/colcon-test-result-0.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583528924
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
