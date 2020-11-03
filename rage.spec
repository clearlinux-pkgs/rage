#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rage
Version  : 0.3.1
Release  : 4
URL      : https://download.enlightenment.org/rel/apps/rage/rage-0.3.1.tar.xz
Source0  : https://download.enlightenment.org/rel/apps/rage/rage-0.3.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: rage-bin = %{version}-%{release}
Requires: rage-data = %{version}-%{release}
Requires: rage-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(elementary)

%description
Rage 0.3.1
******************************************************************************

%package bin
Summary: bin components for the rage package.
Group: Binaries
Requires: rage-data = %{version}-%{release}
Requires: rage-license = %{version}-%{release}

%description bin
bin components for the rage package.


%package data
Summary: data components for the rage package.
Group: Data

%description data
data components for the rage package.


%package license
Summary: license components for the rage package.
Group: Default

%description license
license components for the rage package.


%prep
%setup -q -n rage-0.3.1
cd %{_builddir}/rage-0.3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604362866
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/rage
cp %{_builddir}/rage-0.3.1/COPYING %{buildroot}/usr/share/package-licenses/rage/e39e087903ee286cc96c6b3b0a0b234cd0458b24
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)
/usr/lib64/rage/utils/rage_thumb

%files bin
%defattr(-,root,root,-)
/usr/bin/rage

%files data
%defattr(-,root,root,-)
/usr/share/applications/rage.desktop
/usr/share/icons/hicolor/128x128/apps/rage.png
/usr/share/rage/themes/default.edj

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rage/e39e087903ee286cc96c6b3b0a0b234cd0458b24
