Summary:	cghttpd
Name:		cghttpd
Version:	0.26
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.xmailserver.org/%{name}-%{version}.tar.gz
# Source0-md5:	62a1ae4ecd938954fa86c94e0edaef33
URL:		http://www.xmailserver.org/cghttpd-home.html
BuildRequires:	coronet-devel
BuildRequires:	guasi-devel
BuildRequires:	libpcl-devel
# not yet(?) complete webserver
#Provides:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_sbindir}

%description
The cghttpd software is a Coronet and Guasi based trivial Web server
developed to test the level of performance that can be achieved with
such a solution.

It is by far not a complete Web server, nor a server that you want to
expose to a public network.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_sbindir}/cghttpd
%{_mandir}/man8/cghttpd.8*
