Name:           rlwrap
Version:        0.37
Release:        %mkrel 1
Epoch:          0
Summary:        Readline wrapper
Group:          Text tools
License:        GPL
URL:            http://utopia.knoware.nl/~hlub/rlwrap/
Source0:        http://utopia.knoware.nl/~hlub/rlwrap/rlwrap-%{version}.tar.gz
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  libreadline-devel

%description
rlwrap is a 'readline wrapper' that uses the GNU readline library to
allow the editing of keyboard input for any other command. Input
history is remembered across invocations, separately for each command;
history completion and search work as in bash and completion word
lists can be specified on the command line.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%check
%make check

%files
%doc AUTHORS BUGS COPYING ChangeLog INSTALL NEWS README TODO PLEA
%attr(0755,root,root) %{_bindir}/rlwrap
%{_mandir}/man1/rlwrap.1*
%{_mandir}/man3/RlwrapFilter.3pm*
%dir %{_datadir}/rlwrap
%{_datadir}/rlwrap/*


%changelog
* Sun May 09 2010 Lev Givon <lev@mandriva.org> 0:0.37-1mdv2011.0
+ Revision: 544267
- Update to 0.37.

* Mon Jan 18 2010 Frederik Himpe <fhimpe@mandriva.org> 0:0.36-1mdv2010.1
+ Revision: 493244
- update to new version 0.36

* Sat Jan 09 2010 Frederik Himpe <fhimpe@mandriva.org> 0:0.35-1mdv2010.1
+ Revision: 488145
- update to new version 0.35

* Wed Dec 23 2009 Frederik Himpe <fhimpe@mandriva.org> 0:0.34-1mdv2010.1
+ Revision: 481826
- update to new version 0.34

* Thu Oct 22 2009 Lev Givon <lev@mandriva.org> 0:0.32-1mdv2010.1
+ Revision: 458925
- Update to 0.32.

* Thu May 07 2009 Lev Givon <lev@mandriva.org> 0:0.30-5mdv2010.0
+ Revision: 372777
- Bump release to rebuild against libreadline6.

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0:0.30-4mdv2009.0
+ Revision: 260276
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0:0.30-3mdv2009.0
+ Revision: 251326
- rebuild

* Tue Jan 08 2008 David Walluck <walluck@mandriva.org> 0:0.30-1mdv2008.1
+ Revision: 146920
- 0.30

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 14 2007 David Walluck <walluck@mandriva.org> 0:0.29-1mdv2008.1
+ Revision: 108565
- 0.29


* Mon Dec 18 2006 David Walluck <walluck@mandriva.org> 0.28-1mdv2007.0
+ Revision: 98509
- BuildRequires: libncurses-devel
- Import rlwrap

* Mon Dec 18 2006 David Walluck <walluck@mandriva.org> 0:0.28-1mdv2007.1
- release

