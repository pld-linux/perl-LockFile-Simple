#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	LockFile
%define		pnam	Simple
Summary:	LockFile::Simple Perl module - simple file locking scheme
Summary(pl.UTF-8):	Moduł Perla LockFile::Simple - prosty schemat blokowania plików
Name:		perl-LockFile-Simple
Version:	0.2.5
Release:	4
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	acf9fd6f965789a42fa5314a4be0189d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LockFile::Simple Perl module - provides simple locking scheme which
is not based on any file locking system calls such as "flock()" or
"lockf()" but rather relies on basic file system primitives and
properties, such as the atomicity of the "write()" system call. It is
not meant to be exempt from all race conditions, especially over NFS.

%description -l pl.UTF-8
Moduł Perla LockFile::Simple - udostępnia prosty system blokowania
plików nie oparty na żadnych funkcjach systemowych, takich jak
"flock()" i "lockf()" służących do blokowania plików. Korzysta on z
podstawowych własności systemów plików, takich jak atomowość funkcji
systemowej "write()". Nie oznacza to, że jest on wolny od sytuacji
"wyścigu" (race conditions), zwłaszcza w przypadku korzystania z NFS.

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
%doc ChangeLog README
%{perl_vendorlib}/LockFile/*.pm
%{perl_vendorlib}/LockFile/Lock
%{_mandir}/man3/*
