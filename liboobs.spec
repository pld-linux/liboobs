Summary:	Wrapping library to the System Tools Backends
Summary(pl.UTF-8):	Biblioteka opakowywująca dla System Tools Backends
Name:		liboobs
Version:	2.19.91
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/liboobs/2.19/%{name}-%{version}.tar.bz2
# Source0-md5:	1b9081d3b1e1cae1df9d921b5557bc6c
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	glib2-devel >= 1:2.12.11
BuildRequires:	gtk-doc >= 1.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	system-tools-backends >= 2.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liboobs is a wrapping library to the System Tools Backends. It
provides easy to access GObjects to system configuration details, like
users, groups and network interfaces.

%description -l pl.UTF-8
Liboobs jest biblioteką opakowywującą dla System Tools Backends.
Dostarcza łatwe interfejsy GObjects dla szczegółów konfiguracyjnych,
takich jak użytkownicy, grupy, czy interfejsy sieciowe.

%package devel
Summary:	Header files for liboobs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboobs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.73
Requires:	glib2-devel >= 1:2.12.11
Requires:	system-tools-backends >= 2.3.1

%description devel
Header files for liboobs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liboobs.

%package static
Summary:	Static liboobs library
Summary(pl.UTF-8):	Statyczna biblioteka liboobs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboobs library.

%description static -l pl.UTF-8
Statyczna biblioteka liboobs.

%package apidocs
Summary:	liboobs API documentation
Summary(pl.UTF-8):	Dokumentacja API liboobs
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
liboobs API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API liboobs.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
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
