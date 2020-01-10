Name:           spice-client
Version:        0.8.2
Release:        15%{?dist}
Summary:        Implements the client side of the SPICE protocol
Group:          User Interface/Desktops
License:        LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://www.spice-space.org/download/releases/spice-%{version}.tar.bz2
Source1:        pyparsing.py
Source2:        spice-xpi-client-spicec

Patch1:  0001-client-fix-30s-timeout-regression.patch
Patch2:  0001-client-red_client-fix-broken-switch-host-migration-R.patch
Patch3:  0001-client-setting-monitors-resolution-728252.patch
Patch4:  0001-fix-bug-692833.patch
Patch5:  0002-client-don-t-crash-when-booting-a-Xinerama-setup.patch

#semi-seamless migration support
Patch6:         seamless-0001-server-spice.h-semi-seamless-migration-interface-RHB.patch
Patch7:         seamless-0002-server-handle-migration-interface-addition.patch
Patch8:         seamless-0003-configure-spice-protocol-0.8.2-semi-seamless-migrati.patch
Patch9:         seamless-0004-server-proto-tell-the-client-to-connect-to-the-migra.patch
Patch10:         seamless-0005-spice.proto-add-SPICE_MSG_MAIN_MIGRATE_END-SPICE_MSG.patch
Patch11:         seamless-0006-server-send-SPICE_MSG_MAIN_MIGRATE_END-on-spice_serv.patch
Patch12:         seamless-0007-server-move-SPICE_MSG_MAIN_INIT-sending-code-to-a-se.patch
Patch13:         seamless-0008-server-move-the-linking-of-channels-to-a-separate-ro.patch
Patch14:         seamless-0009-server-handling-semi-seamless-migration-in-the-targe.patch
Patch15:         seamless-0010-server-call-migrate_connect_complete-callback-when-n.patch
Patch16:         seamless-0011-server-turn-spice_server_migrate_start-into-a-valid-.patch
Patch17:         seamless-0012-server-fall-back-to-switch-host-scheme-in-case-semi-.patch
Patch18:         seamless-0013-server-fix-not-calling-migrate_connect-completion-ca.patch
Patch19:         seamless-0014-client-rewrite-surfaces-cache.patch
Patch20:         seamless-0015-client-RedPeer-HostAuthOptions-set_cert_subject.patch
Patch21:         seamless-0016-client-handle-SpiceMsgMainMigrationBegin-for-0.8.2.patch
Patch22:         seamless-0017-client-handle-SPICE_MSG_MAIN_MIGRATE_END.patch
Patch23:         seamless-0018-client-main-channel-migration-do-partial-cleanup-whe.patch
Patch24:         seamless-0019-client-playback-record-channels-implement-on_disconn.patch
Patch25:         seamless-0020-client-display-channel-migration.patch
Patch26:         seamless-0021-client-display-channel-destroy-all-surfaces-on-disco.patch
Patch27:         seamless-0022-client-support-semi-seamless-migration-between-spice.patch
Patch28:         seamless-0023-Release-0.8.3.patch

#bug 695323
Patch30:         0001-client-add-xinerama-support.patch
#bug 693431
Patch31:         0002-client-x11-reset-screen-positions-in-XMonitor-do_res.patch
Patch32:         0003-client-x11-fix-mode-setting-in-MultyMonScreen-restor.patch
Patch33:         0004-client-windows-fix-typo-make-error-messages-unique.patch
#bug 711810
Patch34:         0005-Don-t-use-hw-0-0-for-recording-with-alsa.patch
#bug 750030
Patch35:         0006-Handle-Application-set_hotkeys-failure.patch
#bug 791274
Patch36:         0007-client-handle-the-redundant-right-ctrl-windows-messa.patch
Patch37:         0008-client-handle-the-redundant-right-ctrl-windows-messa.patch
Patch38:         0009-client-controller-foreign_menu-use-memmove-instead-o.patch
#bug 791271
Patch39:         0010-client-menu-make-RedWindow-set_menu-return-an-error-.patch
Patch40:         0011-client-update-menu-if-needed-when-exiting-full-scree.patch
#bug 791269
Patch41:         0012-client-foreign-menu-pass-active-param-when-creating-.patch
#bug 552539
Patch42:         0013-client-keyboard-add-mapping-for-volume-keys.patch
Patch43:         0014-client-X11-support-volume-keys-when-evdev-is-in-use.patch
#bug 641828
Patch44:         0015-client-handle-CONTROLLER_ENABLE_SMARTCARD-rhbz-64182.patch
Patch45:         0016-Fix-compilation-when-smartcard-support-is-disabled.patch
#bug 750856
Patch46:         0017-controller-remember-if-Ctrl-Alt-Del-is-disabled.patch
Patch47:         0018-client-block-CtrlAltDel-if-disabled-by-controller.patch
Patch48:         0019-win32-don-t-unconditionnally-block-ctrl-alt-del.patch
Patch49:         0001-Use-SPICE_FOREIGN_MENU_SOCKET-if-it-s-available.patch
Patch50:         0021-Don-t-limit-spice-controller-socket-name-to-50-chars.patch

BuildRoot:      %{_tmppath}/%{tarname}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch:  i686 x86_64


BuildRequires:  autoconf automake libtool
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  alsa-lib-devel
BuildRequires:  pixman-devel >= 0.18
BuildRequires:  libjpeg-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXinerama-devel
BuildRequires:  openssl-devel
BuildRequires:  celt051-devel
BuildRequires:  libcacard-devel >= 0.1.2
BuildRequires:  spice-protocol >= 0.8.1-2
Requires:       pixman >= 0.18
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package provides the client side of the SPICE protocol


%prep
%setup -q -n spice-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1

%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1

%build
export PYTHONPATH=$(dirname %{SOURCE1})

autoreconf -f -i

%configure --enable-smartcard --without-sasl
make -C client %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make -C client install DESTDIR=$RPM_BUILD_ROOT
# create libexec 0.4 compat link
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
ln -s %{_bindir}/spicec $RPM_BUILD_ROOT%{_libexecdir}/spicec
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
touch $RPM_BUILD_ROOT%{_libexecdir}/spice-xpi-client
install -m 0755 %{_sourcedir}/spice-xpi-client-spicec $RPM_BUILD_ROOT%{_libexecdir}/


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/spicec
%{_libexecdir}/spicec
%ghost %{_libexecdir}/spice-xpi-client
%{_libexecdir}/spice-xpi-client-spicec

%post
%{_sbindir}/update-alternatives --install %{_libexecdir}/spice-xpi-client \
  spice-xpi-client %{_libexecdir}/spice-xpi-client-spicec 21

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove spice-xpi-client %{_libexecdir}/spice-xpi-client-spicec
fi

%changelog
* Thu Mar 22 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.8.2-15
- Actually apply the patch added to -14... Thanks to rpmdiff :)
Related: rhbz#804561

* Wed Mar 21 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.8.2-14
- Don't hardcode a limit for SPICE_XPI_SOCKET length
Resolves: rhbz#804561

* Mon Mar 05 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.8.2-13
- Use foreign menu specified by environment.
Resolves: rhbz#796848

* Mon Mar 05 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.8.2-12
- handle ENABLE_SMARTCARD messages from the controller
  Resolves: rhbz#641828
- handle SEND_CAD messages from the controller
  Resolves: rhbz#750856

* Thu Mar 1 2012 Yonit Halperin <yhalperi@redhat.com> - 0.8.2-11
- send volume keys to the guest
Resolves: rhbz#552539

* Fri Feb 24 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.8.2-10
- sync RHEV (windows client) patches which are upstream
  - fix USB sharing when starting SPICE fullscreen (windows client only)
Resolves: rhbz#791269
  - fix menu issues when USB sharing is enabled (windows client only)
Resolves: rhbz#791271
  - fix issues with AltGr when keyboard layout is non-us (windows client
    only)
Resolves: rhbz#791274

* Thu Feb 23 2012 Marc-Andre Lureau <marcandre.lureau@redhat.com> - 0.8.2-9
- Provides a spice-xpi-client alternative script
Resolves: rhbz#796848

* Wed Feb 15 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.8.2-8
- added upstream patches for various RHEL bugs
  - client: add xinerama support
Resolves: rhbz#695323
  - client/x11: fix mode setting in MultyMonScreen::restore
Resolves: rhbz#693431
  - Don't use "hw:0,0" for recording with alsa
Resolves: rhbz#711810
  - Handle Application::set_hotkeys failure
Resolves: rhbz#750030

* Wed Sep 28 2011 Uri Lublin <uril@redhat.com> - 0.8.2-7
- semi-seamless migration support
- added pyparsing.py as source, and using it to build the package.
- added BuildRequires: autoconf automake libtool and using them.
- applied server patches too
- requires spice-protocol-0.8.1-2 (equivalent to upstream 0.8.2)
- advertise itself as version 0.8.3, to notify the new feature.
Resolves: rhbz#725009

* Tue Sep 20 2011 Christophe Fergeau <cfergeau@redhat.com> - 0.8.2-6
- add upstream patch for bug #692833
Resolves: rhbz#692833
- add upstream patch for bug #732423 client: don't crash when booting a
  Xinerama setup
Resolves: rhbz#732433
- removed old patch from CVS (it was already removed from spec)

* Sun Aug 28 2011 Yonit Halperin <yhalperi@redhat.com> - 0.8.2-5
- used upstream patch instead of 0.8 patch (Alon)
Resolves: rhbz#728252

* Sun Aug 28 2011 Yonit Halperin <yhalperi@redhat.com> - 0.8.2-4
- client: setting monitors resolution before resizing screens
Resolves: rhbz#728252

* Thu Aug 04 2011 Alon Levy <alevy@redhat.com - 0.8.2-3
- client: fix switch-host regression.
Resolves: rhbz#727969

* Mon Aug 01 2011 Uri Lublin <uril@redhat.com> - 0.8.2-2
- client: fix 30s timeout regression (autoconf/effects)
Resolves: rhbz#726441

* Fri Jul 22 2011 Uri Lublin <uril@redhat.com> - 0.8.2-1
- Rebase to upstream spice-0.8.2, including:
  + Bug fixes (RHBZ): 712938, 710461, 673973, 667689, 692976, 712941
Resolves: rhbz#723687

* Fri Jul 22 2011 Uri Lublin <uril@redhat.com> - 0.8.0-3
- Remove Obsolete lines from spec
Resolves: rhbz#707122

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
