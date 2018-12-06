# http://github.com/mistifyio/go-zfs

%global goipath         github.com/mistifyio/go-zfs
%global commit          1b4ae6fb4e77b095934d4430860ff202060169f8


%gometa -i

Name:           golang-github-mistifyio-go-zfs
Version:        0
Release:        0.10%{?dist}
Summary:        Go wrappers for ZFS commands
# Detected licences
# - *No copyright* UNKNOWN at 'LICENSE'
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

ExcludeArch:    aarch64 s390x

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/pborman/uuid)
BuildRequires: zfs-fuse

Requires: zfs-fuse

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
# source codes for building projects
%goinstall glide.lock glide.yaml

%check
# zfs-fuse deamon must be running and the test has to be run under root
#%%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc CONTRIBUTING.md README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git1b4ae6f
- Upload glide files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 26 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git1b4ae6f
- Excluder aarch64 architecture
  resolves: #1465016

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git1b4ae6f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git1b4ae6f
- https://fedoraproject.org/wiki/Changes/golang1.7

* Tue Jun 07 2016 jchaloup <jchaloup@redhat.com> - 0-0.2.git1b4ae6f
- Don't build on arm architectures (missing zfs-fuse)
  resolves: #1341333

* Thu Apr 14 2016 jchaloup <jchaloup@redhat.com> - 0-0.1.git1b4ae6f
- First package for Fedora
  resolves: #1327291
