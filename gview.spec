Summary:	gView is a GTK+ image browser and viewer
Summary(pl):	gView jest przegl±dark± plików graficznych opart± na GTK+
Name:		gview
Version:	0.1.13
Release:	1
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
License:	GPL
Source0:	ftp://ftp.petech.ac.za/pub/viewers/%{name}-%{version}.tar.gz
Source1:	gview.desktop
BuildRequires:	gtk+-devel >= 1.1.9
BuildRequires:	glib-devel >= 1.1.9
BuildRequires:	imlib-devel >= 1.4.0
BuildRequires:	XFree86-devel
URL:		http://gview.netpedia.net/
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define		_applnkdir	%{_datadir}/applnk

%description
gView is an image browser and viewer, using GTK+ and Imlib, that uses a
style similar to that of ACDSee for Windows.

%description -l pl
gView jest przegl±dark± obrazków wykorzystuj±c± biblioteki GTK+ i Imlib,
posiadaj±c± interfejs zbli¿ony do ACDSee dla Windows.

%prep
%setup -q

%build
%configure

make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics/Viewers

make install-strip DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Graphics/Viewers

gzip -9nf README ChangeLog TODO NEWS AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,TODO,NEWS,AUTHORS}.gz
%attr (755,root,root) %{_bindir}/gview

%{_applnkdir}/Graphics/Viewers/gview.desktop
