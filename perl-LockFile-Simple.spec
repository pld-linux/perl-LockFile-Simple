#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	LockFile
%define	pnam	Simple
Summary:	LockFile::Simple Perl module - simple file locking scheme
Summary(pl):	Modu� Perla LockFile::Simple - prosty schemat blokowania plik�w
Name:		perl-LockFile-Simple
Version:	0.2.5
Release:	2
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	acf9fd6f965789a42fa5314a4be0189d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LockFile::Simple Perl module - provides simple locking scheme which
is not based on any file locking system calls such as "flock()" or
"lockf()" but rather relies on basic file system primitives and
properties, such as the atomicity of the "write()" system call. It is
not meant to be exempt from all race conditions, especially over NFS.

%description -l pl
Modu� Perla LockFile::Simple - udost�pnia prosty system blokowania
plik�w nie oparty na �adnych funkcjach systemowych, takich jak
"flock()" i "lockf()" s�u��cych do blokowania plik�w. Korzysta on z
podstawowych w�asno�ci system�w plik�w, takich jak atomowo�� funkcji
systemowej "write()". Nie oznacza to, �e jest on wolny od sytuacji
"wy�cigu" (race conditions), zw�aszcza w przypadku korzystania z NFS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/LockFile/*.pm
%{perl_vendorlib}/LockFile/Lock
%{_mandir}/man3/*
