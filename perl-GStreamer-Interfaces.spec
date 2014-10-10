%define upstream_name    GStreamer-Interfaces
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Perl module for the gstreamer library
License:    GPL+ or Artistic
Group:      Development/GNOME and GTK+
Url:        http://gtk2-perl.sf.net/
Source0:    %{upstream_name}-%{upstream_version}.tar.gz
# http://sourceforge.net/project/showfiles.php?group_id=64773&package_id=150831

BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	perl(Glib) >= 1.100
BuildRequires:	perl(GStreamer)
BuildRequires:	perl(Gtk2) >= 1.100
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl-devel

%description
This module allows you to use the GStreamer library from Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"

%check
#%make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{perl_vendorarch}/GStreamer/*
%{perl_vendorarch}/auto/*

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.60.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 555899
- rebuild for perl 5.12

* Mon Mar 22 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 526442
- update to 0.06

* Sun Mar 07 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 515362
- update to 0.05

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 408415
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2009.0
+ Revision: 268513
- rebuild early 2009.0 package (before pixel changes)

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 0.04-1mdv2009.0
+ Revision: 192889
- new release

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.03-4mdv2008.1
+ Revision: 152100
- rebuild

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-3mdv2008.1
+ Revision: 138074
- fix build dependencies

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.03-2mdv2007.0
- fix buildrequires

* Tue Jul 25 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.03-1mdv2007.0
- initial release

