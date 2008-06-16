# - see php-magickwand.spec
Summary:	MagickWand ImageMagick API for PHP
Summary(pl.UTF-8):	API ImageMagick MagickWand dla PHP
Name:		MagickWandForPHP
Version:	1.0.5
Release:	2
License:	ImageMagick (Apache-like)
Group:		Libraries
Source0:	http://www.magickwand.org/download/php/%{name}-%{version}.tar.bz2
# Source0-md5:	b52a5b7cf4db7078fa3db4cb6e55ecf4
Source1:	%{name}.ini
URL:		http://www.magickwand.org/
BuildRequires:	ImageMagick-devel >= 6.3.5.9
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%requires_eq	php-common
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MagickWand API is the recommended interface between the C
programming language and the ImageMagick image processing libraries.
Unlike the MagickCore C API, MagickWand uses only a few opaque types.
Accessors are available to set or get important wand properties.

%description -l pl.UTF-8
API MagickWand jest zalecanym interfejsem między językiem C a
bibliotekami przetwarzania obrazu ImageMagick. W przeciwieństwie do
API C MagickCore, MagickWand używa tylko kilku nieprzejrzystych typów.
Dostępne są funkcje dostępowe do ustawiania i pobierania istotnych
właściwości wand.

%prep
%setup -q

%build
phpize
%configure \
	--with-php-config=%{_bindir}/php-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_extensiondir},%{php_sysconfdir}/conf.d}

install modules/magickwand.so $RPM_BUILD_ROOT%{php_extensiondir}
install %{SOURCE1} $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_name}.ini

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
%doc AUTHOR CREDITS ChangeLog LICENSE README TODO run-tests.php
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_name}.ini
%attr(755,root,root) %{php_extensiondir}/magickwand.so
