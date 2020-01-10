Name:           spice-client
Version:        0.8.0
Release:        2%{?dist}.1
Summary:        Implements the client side of the SPICE protocol
Group:          User Interface/Desktops
License:        LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/spice-%{version}.tar.bz2
# rhbz: 675767
Patch0:         0001-client-Don-t-handle-hotkeys-while-sticky-alt-is-acti.patch
BuildRoot:      %{_tmppath}/%{tarname}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:  i686 x86_64

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  alsa-lib-devel
BuildRequires:  pixman-devel >= 0.18
BuildRequires:  libjpeg-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  openssl-devel
BuildRequires:  celt051-devel
BuildRequires:  libcacard-devel >= 0.1.2
BuildRequires:  spice-protocol >= 0.7.0
Requires:       pixman >= 0.18


%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package provides the client side of the SPICE protocol


%prep
%setup -q -n spice-%{version}
%patch0 -p1


%build
%configure --enable-smartcard
make -C client %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make -C client install DESTDIR=$RPM_BUILD_ROOT
# create libexec 0.4 compat link
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
ln -s %{_bindir}/spicec $RPM_BUILD_ROOT%{_libexecdir}/spicec


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/spicec
%{_libexecdir}/spicec


%changelog
* Thu Sep 15 2011 Uri Lublin <uril@redhat.com> - 0.8.0-2.1
- Remove Obsolete lines from spec
Resolves: rhbz#725103

* Fri Mar 11 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-2
- Fix being unable to send ctrl+alt+key when release mouse is bound to
  ctrl+alt (which can happen when used from RHEV-M)
Resolves: rhbz#675767

* Wed Mar  2 2011 Hans de Goede <hdegoede@redhat.com> - 0.8.0-1
- Rebase to new upstream release 0.8.0
Resolves: rhbz#671383
- Exit with error instead of crash for --controller with no SPICE_XPI_SOCKET
Resolves: rhbz#644292
- Use _exit rather then exit on X errors
Resolves: rhbz#680763
- Fix keyb modifiers not syncing from guest to client
Resolves: rhbz#679467

* Mon Feb 14 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.3-1
- Rebase to new upstream release 0.7.3
Related: rhbz#671383

* Fri Feb 04 2011 Uri Lublin <uril@redhat.com> - 0.7.2-4
- Remove spice-client watermark.
Resolves: #655029

* Fri Feb 04 2011 Uri Lublin <uril@redhat.com> - 0.7.2-3
- smartcard -- libcacard 0.1.2 updates:
 - server (not part of this package -- in spice-server)
  - use network byte order when talking to device.
 - both
  - no more reader_id_t, uint32_t instead
  - no more ReaderAddResponse, use VSC_Error with
    code==VSC_SUCCESS instead.
  - change an assert to a red_printf("error:..")
    if got an unexpectedly undefined reader id.
 - client
  - track number of expected reader insertions
Resolves: #641829

* Fri Feb 04 2011 Uri Lublin <uril@redhat.com> - 0.7.2-2
- Obsolete old packages that are not needed now
Resolves: #675085

* Tue Jan 25 2011 Hans de Goede <hdegoede@redhat.com> - 0.7.2-1
- Rebase to new upstream release 0.7.2
  Resolves: rhbz#671383
- This fixes:
- Blinking keyb leds in spice client causes capslock to turn on / off
  all the time in other windows
  Resolves: rhbz#626975
- jpeg messages encoding is transfered as 4 and not 1, breaking client
  Resolves: rhbz#670238
- fix warnings from AC_COMPILE_IFELSE
  Resolves: rhbz#670271
- Clearer error message when subject-host differs from server
  Resolves: rhbz#670274
- long arguments are incorrectly parsed when an equal sign is used
  Resolves: rhbz#670276

* Fri Dec 17 2010 Hans de Goede <hdegoede@redhat.com> - 0.7.1-1
- New upstream release 0.7.1
- Drop all patches (all upstreamed)
- Enable smartcard (CAC) support
  Related: rhbz#641829

* Thu Nov 25 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-8
- Add fixes from upstream git for a number of serious bugs:
  - ctrl / alt getting stuck
  - a client hang
  - a client crash
  - showing nothing but a white screen in fullscreen mode
  Related: rhbz#644258

* Tue Nov 16 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-7
- Add explicit Requires for pixman >= 0.18                      
  Related: rhbz#644258

* Tue Nov  9 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-6
- Fix the watermark and sticky key notifications not being shown
  Related: rhbz#644258

* Wed Oct 20 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-5
- Fix the spicec window not being on top when first shown
  Related: rhbz#644258

* Wed Oct 20 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-4
- Fix spice-xpi/qspice-client unix socket race again (rhbz#644854)
- Fix setting window title from xpi
  Related: rhbz#644258

* Tue Oct 19 2010 Hans de Goede <hdegoede@redhat.com> - 0.6.3-3
- New upstream release 0.6.3
  Resolves: rhbz#644258

* Wed Aug 4 2010 Martin Stransky <stransky@redhat.com> - 0.4.2-18
- fix spice-xpi/qspice-client unix socket race
  Resolves: #620444

* Fri Jul 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-17
 - fix unsafe guest/host data handling
 Resolves: #568811

* Tue Jun 29 2010 Uri Lublin <uril@redhat.com> - 0.4.2-16
- remove BuildRequires mesa-libGLU-devel
  + open-gl is now disabled.
Related: #482556

* Tue Jun 29 2010 Uri Lublin <uril@redhat.com> - 0.4.2-15
 - make opengl optional, disabled by default
Resolves: #482556

* Tue Jun 29 2010 Uri Lublin <uril@redhat.com> - 0.4.2-14
 - client: spicec --full-screen=auto-conf do not resize after migration
Resolves: #584318

* Tue Jun 29 2010 Uri Lublin <uril@redhat.com> - 0.4.2-13
 - client: log warnings and errors to stderr too
Resolves: #580925

* Mon Jun 21 2010 Uri Lublin <uril@redhat.com> - 0.4.2-12
 - client: x11: call getsockname() with initizlized sock_len
 Resolves: #604701

* Sun Apr  4 2010 Uri Lublin <uril@redhat.com> - 0.4.2-11
 - client: x11: fix a crash caused by a call to a destroyed window
Resolves: #578458

* Sun Apr  4 2010 Uri Lublin <uril@redhat.com> - 0.4.2-10
 - Add glext_proto.h file to client/Makefile.am
Related: #576639

* Sun Apr  4 2010 Uri Lublin <uril@redhat.com> - 0.4.2-9
 - generate auto* generated files (e.g. Makefile.in)
Resolves: #579328

* Wed Mar 24 2010 Uri Lublin <uril@redhat.com> - 0.4.2-8
 - support for building windows client using VS2008
 - also fixed a typo in 0.4.2-7
Resolves: #576639

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-7
 - spice: client: add foreign menu
 - spice: client: add controller
 - spice: client: fix controller & foreign menu review comments
Resolves: #558248
Resolves: #558247

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-6
 - spice: client: x11: install spicec in /usr/libexec
Resolves: #576437

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-5
 - fix handling of top down images in video streams
Resolves: #576151

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-4
 - new migration process
Resolves: #576031

* Thu Mar 18 2010 Uri Lublin <uril@redhat.com> - 0.4.2-3
- fix dns lookup
- enable ipv6
Resolves: #566444

* Thu Mar 18 2010 Uri Lublin <uril@redhat.com> - 0.4.2-2
- add command line support for ciphers, ca file, and host certificate subject
Resolves: #573371

* Mon Mar  1 2010 Uri Lublin <uril@redhat.com> - 0.4.2-1
 - This package does not "Requires: pkgconfig" (removed).
Related: #543948

* Mon Jan 11 2009 Uri Lublin <uril@redhat.com> - 0.4.2-0
 - first spec for 0.4.2
Related: #549814
