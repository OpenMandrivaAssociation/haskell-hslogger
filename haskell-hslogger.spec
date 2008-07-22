%define module hslogger

Name: haskell-%{module}
Version: 1.0.1
Release: %mkrel 6
Summary: Logging framework for Haskell
Group: Development/Other
License: LGPL
Url: http://software.complete.org/hslogger
Source: http://software.complete.org/hslogger/static/download_area/%{version}/hslogger_%{version}.tar.bz2
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
%setup -q -n %{module}

%build
%_cabal_build

%_cabal_genscripts

%check
%_cabal_check

%install
%_cabal_install

rm -fr %{buildroot}/%_datadir/*/doc/

%_cabal_rpm_gen_deps

%_cabal_scriptlets

%files
%defattr(-,root,root)
%doc dist/doc/html
%_libdir/*
%_cabal_rpm_files

%clean
rm -fr %buildroot


