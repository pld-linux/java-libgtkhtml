%define	pname	libgtkhtml-java
%define	api	2.7
%define	gtkapi	2.4
Summary:	Java interface for libgtkhtml
Summary(pl.UTF-8):   Wrapper Java dla libgtkhtml
Name:		java-libgtkhtml
Version:	2.7.2
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/java-gnome/%{pname}-%{version}.tar.bz2
# Source0-md5:	9a203dbe85525c51863b0c23fe5b866a
Patch0:		%{name}-configure.patch
Patch1:		%{name}-version_vars.patch
Patch2:		%{name}-typo.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.3
BuildRequires:	java-gtk-devel >= 2.4.2
BuildRequires:	libgcj-devel >= 3.3.2
BuildRequires:	libgtkhtml-devel >= 2.6.2
BuildRequires:	slocate
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for libgtkhtml.

%description -l pl.UTF-8
Wrapper Java dla libgtkhtml.

%package devel
Summary:	Header files for java-libgtkhtml library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki java-libgtkhtml
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for java-libgtkhtml library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki java-libgtkhtml.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
gtkhtmlapiversion="%{api}"; export gtkhtmlapiversion
gtkhtmlversion="%{version}"; export gtkhtmlversion
gtkapiversion="%{gtkapi}"; export gtkapiversion
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/java-gnome,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gnome/*
