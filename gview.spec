Summary:	gView is a GTK+ image browser and viewer
Summary(pl):	gView jest przegl±dark± plików graficznych opart± na GTK+
Name:		gview
Version:	0.1.15
Release:	1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
License:	GPL
Source0:	ftp://ftp.petech.ac.za/pub/viewers/%{name}-%{version}.tar.gz
Source1:	gview.desktop
Patch0:		gview-automake.patch
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.1.9
BuildRequires:	imlib-devel >= 1.4.0
URL:		http://gview.netpedia.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

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
automake
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Graphicsdir=%{_applnkdir}/Graphics/Viewers

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

gzip -9nf README ChangeLog TODO NEWS AUTHORS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO,NEWS,AUTHORS}.gz
%attr(755,root,root) %{_bindir}/gview
%{_applnkdir}/Graphics/Viewers/gview.desktop
