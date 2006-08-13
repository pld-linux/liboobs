Summary:	Wrapping library to the System Tools Backends
Summary(pl):	Biblioteka opakowywuj±ca dla System Tools Backends
Name:		liboobs
Version:	0.2.0
Release:	1
License:	GPL/LGPL/BSD/BSD-like/other license name here)
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/liboobs/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	20a9ffc401c0da4d9119ddf250931a07
URL:		http://www.gnome.org/
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	system-tools-backends >= 1.9.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liboobs is a wrapping library to the System Tools Backends. It
provides easy to access GObjects to system configuration details, like
users, groups and network interfaces.

%description -l pl
Liboobs jest bibliotek± opakowywuj±c± dla System Tools Backends.
Dostarcza ³atwe interfejsy GObjects dla szczegó³ów konfiguracyjnych,
takich jak u¿ytkownicy, grupy, czy interfejsy sieciowe.

%package devel
Summary:	Header files for liboobs library
Summary(pl):	Pliki nag³ówkowe biblioteki liboobs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for liboobs library.

%description devel -l pl
Pliki nag³ówkowe biblioteki liboobs.

%package static
Summary:	Static liboobs library
Summary(pl):	Statyczna biblioteka liboobs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboobs library.

%description static -l pl
Statyczna biblioteka liboobs.

%prep
%setup -q

%build
%configure \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}-1.0
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
