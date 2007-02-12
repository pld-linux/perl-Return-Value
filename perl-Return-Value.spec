#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Return
%define	pnam	Value
Summary:	Return::Value - Polymorphic Return Values
Summary(pl.UTF-8):   Return::Value - Polimorficzne zwracanie wartości
Name:		perl-Return-Value
Version:	1.301
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	15aeae9a075d58431c2656ec0e2f6cb3
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More) >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Polymorphic return values are really useful. Often, we just want to
know if something worked or not. Other times, we'd like to know what
the error text was. Still others, we may want to know what the error
code was, and what the error properties were. We don't want to handle
objects or data structures for every single return value, but we do
want to check error conditions in our code because that's what good
programmers do.

When functions are successful they may return true, or perhaps some
useful data. In the quest to provide consistent return values, this
gets confusing between complex, informational errors and successful
return values.

This module provides these features with a simple API that should get
you what you're looking for in each context a return value is used in.

%description -l pl.UTF-8
Polimorficzne wartości zwracane bywają naprawdę przydatne. Często
chcemy tylko wiedzieć, czy coś zadziałało, czy nie. Innym razem
chcielibyśmy poznać tekstową postać błędu. W jeszcze innym przypadku
możemy chcieć poznać kod błędu i jego właściwości. Nie chcemy
obsługiwać obiektów czy struktur danych dla każdej zwracanej wartości,
ale chcemy sprawdzić w naszym kodzie wystąpienie błędu, ponieważ tak
robią dobrzy programiści.

W przypadku sukcesu funkcje mogą zwrócić wartość true albo jakieś
przydatne dane. Przy poszukiwaniu sposobu dostarczenia spójnych
wartości błędów, staje się to coraz bardziej zagmatwane pomiędzy
złożonymi, informacyjnymi błędami a poprawnymi zwracanymi wartościami.

Ten moduł dostarcza te możliwości z prostym API, które powinno
zapewnić to, czego szukamy w każdym kontekście wykorzystania zwracanej
wartości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Return/Value.pm
%{_mandir}/man3/*
