Summary: 	Scratchbox2 crosscompiling environment
License: 	LGPL
URL:	        https://git.sailfishos.org/mer-core/scratchbox2
Name: 		scratchbox2
Version:	2.3.90
Release:	0
Source: 	%{name}-%{version}.tar.gz
Prefix: 	/usr
ExclusiveArch:	%{ix86}
BuildRequires:	make
BuildRequires:	autoconf
BuildRequires:  pkgconfig(lua)
Requires:	fakeroot
Requires:	libsb2 = %{version}-%{release}

%description
Scratchbox2 crosscompiling environment

%package -n libsb2
Summary: Scratchbox2 preload library

%description -n libsb2
Scratchbox2 preload library.

%package docs
Summary: Scratchbox2 docs

%description docs
Scratchbox2 man pages.

%prep
%setup -q -n %{name}-%{version}

%build
./autogen.sh
./configure; touch .configure
make

%install
make install prefix=%{buildroot}/usr

install -D -m 644 utils/sb2.bash %{buildroot}/etc/bash_completion.d/sb2.bash

%files
%defattr(-,root,root)
%{_bindir}/sb2*
%{_datadir}/scratchbox2/*
%config %{_sysconfdir}/bash_completion.d/sb2.bash

%files docs
%doc %attr(0444,root,root) /usr/share/man/man1/*
%doc %attr(0444,root,root) /usr/share/man/man7/*

%files -n libsb2
%defattr(-,root,root)
%{_libdir}/libsb2/*
%ifarch x86_64
/usr/lib32/libsb2/*
%endif
