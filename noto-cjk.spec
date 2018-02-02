#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : noto-cjk
Version  : 2017.06.01.serif.cjk.1.1
Release  : 4
URL      : http://localhost/cgit/projects/noto-cjk/snapshot/noto-cjk-2017-06-01-serif-cjk-1-1.tar.bz2
Source0  : http://localhost/cgit/projects/noto-cjk/snapshot/noto-cjk-2017-06-01-serif-cjk-1-1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : OFL-1.1
Requires: noto-cjk-data

%description
URL: http://noto.googlecode.com/
Version: 1.002
License: SIL Open Font License v1.1
License File: LICENSE

%package data
Summary: data components for the noto-cjk package.
Group: Data

%description data
data components for the noto-cjk package.


%prep
%setup -q -n noto-cjk-2017-06-01-serif-cjk-1-1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1510693488
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1510693488
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/fonts/noto-cjk/NotoSansCJK-Black.ttc
/usr/share/fonts/noto-cjk/NotoSansCJK-Bold.ttc
/usr/share/fonts/noto-cjk/NotoSansCJK-DemiLight.ttc
/usr/share/fonts/noto-cjk/NotoSansCJK-Light.ttc
/usr/share/fonts/noto-cjk/NotoSansCJK-Medium.ttc
/usr/share/fonts/noto-cjk/NotoSansCJK-Regular.ttc
/usr/share/fonts/noto-cjk/NotoSansCJK-Thin.ttc
