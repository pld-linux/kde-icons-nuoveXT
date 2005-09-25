#$Revision: 1.1 $, $Date: 2005-09-25 16:54:30 $

%define         _name nuoveXT

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	1.5
Release:	1
License:	Creative Commons Attribution-NonCommercial-ShareAlike 2.5 License
Group:		Themes
Source0:	http://nuovext.pwsp.net/files/%{_name}-kde-%{version}.tar.gz
# Source0-md5:	3d8d4997909b9717b78a4fcf05ad01e2
URL:		http://www.kde-look.org/content/show.php?content=26449
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is an icon theme with a MacOsX character.

%description -l pl
%{_name} to motyw ikon z charakterem MacOsX.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
