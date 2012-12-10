%define module hslogger

Name: haskell-%{module}
Version: 1.0.7
Release: %mkrel 4
Summary: Logging framework for Haskell
Group: Development/Other
License: LGPL
Url: http://software.complete.org/hslogger
Source: http://software.complete.org/hslogger/static/download_area/%{version}/hslogger-%{version}.tar.gz
BuildRoot: %_tmppath/%name-%version-%release-root
BuildRequires: ghc
BuildRequires: haddock
BuildRequires: haskell-macros

%description
hslogger is a logging framework for Haskell, roughly similar to Python's
logging module.

hslogger has a number of features:
  o Each log message has a priority and a source associated with it 
  o Multiple log writers can be on the system 
  o Configurable global actions based on priority and source 
  o Extensible log writers (handlers) 
  o Default handlers that write to the console, file handles, or syslog 
  o Easy to use operation

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%doc dist/doc/html
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-4mdv2011.0
+ Revision: 611062
- rebuild

* Sun Nov 08 2009 Olivier Thauvin <nanardon@mandriva.org> 1.0.7-3mdv2010.1
+ Revision: 463208
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Mar 12 2009 Olivier Thauvin <nanardon@mandriva.org> 1.0.7-1mdv2009.1
+ Revision: 354065
- 1.0.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix description-line-too-long
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 07 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-4mdv2008.0
+ Revision: 81494
- rebuild


* Wed Mar 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-3mdv2007.1
+ Revision: 143300
- rebuild again

* Mon Mar 12 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-2mdv2007.1
+ Revision: 141554
- rebuild with haskell provides

* Sun Mar 04 2007 Olivier Thauvin <nanardon@mandriva.org> 1.0.1-1mdv2007.1
+ Revision: 132716
- initial mdv package
- Create haskell-hslogger

