Name:           libasn1c
Version:        0.9.38
Release:        1.dcbw%{?dist}
License:        BSD-2-Clause
Summary:        Runtime library of Lev Walkin's asn1c

URL:            https://github.com/osmocom/libasn1c

BuildRequires:  git make gcc autoconf automake libtool
BuildRequires:  pkgconf-pkg-config libtalloc-devel

Source0: %{name}-%{version}.tar.bz2


%description
Runtime library of Lev Walkin's asn1c

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}.


%prep
%autosetup -p1

%build
%global optflags %(echo %optflags | sed 's|-Wp,-D_GLIBCXX_ASSERTIONS||g')
autoreconf -fi
%configure --enable-shared \
           --disable-static

# Fix unused direct shlib dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

find %{buildroot} -name '*.la' -exec rm -f {} \;
sed -i -e 's|UNKNOWN|%{version}|g' %{buildroot}/%{_libdir}/pkgconfig/*.pc


%check
make check


%ldconfig_scriptlets


%files
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Jun  8 2025 Dan Williams <dan@ioncontrol.co> - 0.9.38
- Update to 0.9.38

* Tue Aug 25 2020 Cristian Balint <cristian.balint@gmail.com>
- github update releases
