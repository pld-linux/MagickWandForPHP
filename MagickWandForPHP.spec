Summary:	MagickWand ImageMagick API for PHP
Name:		MagickWandForPHP
Version:	1.0.5
Release:	0.1
License:	GPL
Group:		Libraries
Source0:	http://www.magickwand.org/download/php/%{name}-%{version}.tar.bz2
# Source0-md5:	b52a5b7cf4db7078fa3db4cb6e55ecf4
Source1:	%{name}.ini
URL:		http://eaccelerator.net/
BuildRequires:	ImageMagick-devel >= 6.3.5.9
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%requires_eq	php-common
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
#Requires:	php-zlib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{_name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
The MagickWand API is the recommended interface between the C programming
language and the ImageMagick image processing libraries. Unlike the
MagickCore C API, MagickWand uses only a few opaque types. Accessors are
available to set or get important wand properties.

%prep
%setup -q

%build
phpize
%configure \
	--with-php-config=%{_bindir}/php-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{php_extensiondir},%{_bindir},%{php_sysconfdir}/conf.d,%{_sysconfdir},%{_appdir}}

#install modules/eaccelerator.so $RPM_BUILD_ROOT%{php_extensiondir}
#install eLoader/modules/eloader.so $RPM_BUILD_ROOT%{php_extensiondir}
#install %{SOURCE1} $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_name}.ini

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog NEWS README README.eLoader bugreport.php doc/php
#%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_name}.ini
#%attr(755,root,root) %{php_extensiondir}/eaccelerator.so
#%attr(755,root,root) %{php_extensiondir}/eloader.so
