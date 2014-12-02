Summary: A GNU tool for automatically creating Makefiles
Name: FSP-automake
Version: 1.14.1
Release: 1
License: GPLv2+ and GFDL
Group: Development/Tools
URL: http://www.gnu.org/software/automake/
Source0: automake-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?FSP_PUB: %define FSP_PUB /opt/fsp/pub}
%define install_path %{FSP_PUB}/autotools

Requires: FSP-autoconf >= 2.69
BuildRequires: FSP-autoconf >= 2.69

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles. If you install Automake, you will also need to install
GNU's Autoconf package.

%prep
%setup -n automake-%{version}

%build
export PATH=%{install_path}/bin:$PATH
./configure --prefix=%{install_path}

%install
make %{?_smp_mflags} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{FSP_PUB}
%{FSP_PUB}/autotools


%changelog
* Mon Sep 15 2014  <karl.w.schulz@intel.com> - 
- Initial build.

