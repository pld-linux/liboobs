#
# Conditional build:
%bcond_with	hal	# HAL support

Summary:	Wrapping library to the System Tools Backends
Summary(pl.UTF-8):	Biblioteka opakowująca dla System Tools Backends
Name:		liboobs
Version:	3.0.0
Release:	3
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/liboobs/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	fc3235b902a1cb7ac45776431004a57b
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	gtk-doc >= 1.9
%{?with_hal:BuildRequires:	hal-devel >= 0.5.10}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	system-tools-backends-devel >= 2.10.1
Requires:	dbus-glib >= 0.74
Requires:	glib2 >= 1:2.14.0
%{?with_hal:Requires:	hal-libs >= 0.5.10}
Suggests:	system-tools-backends >= 2.10.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Liboobs is a wrapping library to the System Tools Backends. It
provides easy to access GObjects to system configuration details, like
users, groups and network interfaces.

%description -l pl.UTF-8
Liboobs jest biblioteką opakowującą dla System Tools Backends.
Dostarcza łatwo dostępne interfejsy GObject dla szczegółów
konfiguracyjnych, takich jak użytkownicy, grupy, czy interfejsy
sieciowe.

%package devel
Summary:	Header files for liboobs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboobs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.74
Requires:	glib2-devel >= 1:2.14.0

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
BuildArch:	noarch

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
%{__autoheader}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	%{?with_hal:--with-hal} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/liboobs-1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboobs-1.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboobs-1.so
%{_includedir}/liboobs-1.0
%{_pkgconfigdir}/liboobs-1.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liboobs-1.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
