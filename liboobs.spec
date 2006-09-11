Summary:	Wrapping library to the System Tools Backends
Summary(pl):	Biblioteka opakowywuj±ca dla System Tools Backends
Name:		liboobs
Version:	0.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/liboobs/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	72a0c44193715d8c7ef17cf40df7c42f
URL:		http://www.gnome.org/
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	glib2-devel >= 1:2.12.3
BuildRequires:	gtk-doc >= 1.7
BuildRequires:	pkgconfig
BuildRequires:	system-tools-backends >= 1.9.5.1
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
Requires:	dbus-glib-devel >= 0.71
Requires:	glib2-devel >= 1:2.12.3
Requires:	system-tools-backends >= 1.9.5.1

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

%package apidocs
Summary:	liboobs API documentation
Summary(pl):	Dokumentacja API liboobs
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
liboobs API documentation.

%description apidocs -l pl
Dokumentacja API liboobs.

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

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
