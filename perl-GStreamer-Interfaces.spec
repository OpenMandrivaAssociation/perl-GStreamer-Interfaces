%define module GStreamer-Interfaces
%define	fmodule	GStreamer/Interfaces

Summary: Perl module for the gstreamer library
Name:    perl-%module
Version: 0.04
Release: %mkrel 2
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=150831
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-Glib >= 1.100
BuildRequires: perl-Gtk2 >= 1.100
BuildRequires: libgstreamer-devel >= 0.10
BuildRequires: perl-ExtUtils-Depends
BuildRequires: perl-ExtUtils-PkgConfig
BuildRequires: perl-devel
BuildRequires: perl-GStreamer
BuildRequires: libgstreamer-plugins-base-devel

%description
This module allows you to use the GStreamer library from Perl.

%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
#%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%{_mandir}/*/*
%{perl_vendorarch}/GStreamer
%{perl_vendorarch}/%fmodule
%{perl_vendorarch}/auto/*

