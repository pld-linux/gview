Summary:	gView is a GTK+ image browser and viewer
Summary(pl):	gView jest przegl±dark± plików graficznych opart± na GTK+
Name:		gview
Version:	0.1.15
Release:	4
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.petech.ac.za/pub/viewers/%{name}-%{version}.tar.gz
# Source0-md5:	f54227f9604c57b07ef2678c00d6ab4a
Source1:	%{name}.desktop
Patch0:		%{name}-automake.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.1.9
BuildRequires:	imlib-devel >= 1.4.0
URL:		http://gview.netpedia.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
gView is an image browser and viewer, using GTK+ and Imlib, that uses
a style similar to that of ACDSee for Windows.

%description -l pl
gView jest przegl±dark± obrazków wykorzystuj±c± biblioteki GTK+ i
Imlib, posiadaj±c± interfejs zbli¿ony do ACDSee dla Windows.

%prep
%setup -q
%patch -p1

%build
rm -rf missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics/Viewers

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO NEWS AUTHORS
%attr(755,root,root) %{_bindir}/gview
%{_applnkdir}/Graphics/Viewers/gview.desktop
