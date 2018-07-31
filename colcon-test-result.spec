#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-test-result
Version  : 0.3.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/d7/fb/7c0977c84e732c493843c8461ed0dfa7733b72028d46b4848b0820029134/colcon-test-result-0.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d7/fb/7c0977c84e732c493843c8461ed0dfa7733b72028d46b4848b0820029134/colcon-test-result-0.3.0.tar.gz
Summary  : Extension for colcon to provide information about the test results.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-test-result-python3
Requires: colcon-test-result-python
Requires: colcon-core
BuildRequires : buildreq-distutils3

%description
==================

%package python
Summary: python components for the colcon-test-result package.
Group: Default
Requires: colcon-test-result-python3

%description python
python components for the colcon-test-result package.


%package python3
Summary: python3 components for the colcon-test-result package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-test-result package.


%prep
%setup -q -n colcon-test-result-0.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533003119
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
