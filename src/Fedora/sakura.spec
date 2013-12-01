# Review at https://bugzilla.redhat.com/show_bug.cgi?id=496166

Name:           sakura
Version:        3.1.0
Release:        101.dark%{?dist}
Summary:        Terminal emulator based on GTK and VTE

Group:          User Interface/X
License:        GPLv2
URL:            https://launchpad.net/sakura
Source0:        https://launchpad.net/sakura/trunk/%{version}/+download/sakura-%{version}.tar.bz2
Patch0:         sakura-%{?version}-dark.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  pkgconfig(glib-2.0) >= 2.20
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vte-2.90) >= 0.28
BuildRequires:  cmake desktop-file-utils gettext /usr/bin/pod2man

%description
Sakura is a terminal emulator based on GTK and VTE. It's a terminal emulator 
with few dependencies, so you don't need a full GNOME desktop installed to 
have a decent terminal emulator.


%prep
%setup -q
%patch0 -p1


%build
find . -type f -name CMakeCache.txt -exec rm -rf {} \;
%cmake CMAKE_C_FLAGS="%{optflags}" .
make VERBOSE=1 %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
desktop-file-install \
  --delete-original \
  --remove-category=Utility \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# location of the docs is hardcoded, so we remove them
rm -rf %{buildroot}%{_datadir}/doc/


#%check
#ctest .


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS GPL INSTALL
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/terminal-tango.svg
%{_mandir}/man1/%{name}.1.*


%changelog
* Tue Jun 25 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0

* Mon Feb 19 2013 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.4-3
- Use upsteam patch instead of hack to fix #861451
- BR /usr/bin/pod2man for manpage generation
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Sep 29 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.4-2
- Build with %%{optflags} (#861451)

* Thu Sep 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 3.0.4-1
- Update to 3.0.4 (#860958)
- Build against GTK3 and VTE3
- Change website and source URL to new location at launchpad.net

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.4.2-2
- Rebuild for new libpng

* Sat Jul 30 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.2-1
- Update tp 2.4.2
- Fixes #722686, so remove the patch

* Sun Jul 17 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.1-3
- Bring back the cflags patch as actually this is not fixed (#722793)

* Sat Jul 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.1-2
- Fix crash in  (#722686)
- Remove cflags patch, fixed upstream
- Remove sed hack for pod2man now that it does understand the -u option
- Remove fix for the icon in the desktop file as it's now upstream, too

* Sat Jul 16 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.1-1
- Update to 2.4.1 (fixes #713822)

* Sat Feb 12 2011 Christoph Wickert <cwickert@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.8-1
- Update to 2.3.8

* Wed Apr 07 2010 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.7-1
- Update to 2.3.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.3-3
- Rebuilt for libvte SONAME bump

* Sun Apr 19 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.3-2
- Add patch to honor RPM_OPT_FLAGS
- Include INSTALL in %%doc since it contains some valuable information

* Sat Apr 11 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Tue Nov 11 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.2-1
- Update to 2.3.2

* Sat Nov 01 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Sun Sep 28 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.3.0-1
- Update to 2.3.0

* Sun Sep 21 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.1-1
- Update to 2.2.1
- Disable %%check again

* Fri Jun 20 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Enable %%check again

* Fri Jun 06 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.2-1
- Update to 2.1.2
- No test configuration, disable %%check temporarily 

* Mon May 12 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Mon May 05 2008 Christoph Wickert <cwickert@fedoraproject.org> - 2.0.2-1
- Initial Fedora RPM
