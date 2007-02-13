#$Revision: 1.5 $, $Date: 2007-02-13 08:06:36 $

%define		_name nuoveXT

Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.6
Release:	1
License:	GPL
Group:		Themes
Source0:	http://nuovext.pwsp.net/files/%{_name}-kde-%{version}.tar.gz
# Source0-md5:	5667676200403755c171b48904961f39
URL:		http://www.kde-look.org/content/show.php?content=26449
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is an icon theme with a MacOsX character.

%description -l pl.UTF-8
%{_name} to motyw ikon z charakterem MacOsX.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}
rm $RPM_BUILD_ROOT%{_iconsdir}/*/*~

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
