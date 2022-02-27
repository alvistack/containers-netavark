%global debug_package %{nil}

Name: podman-netavark
Epoch: 100
Version: 1.0.3
Release: 1%{?dist}
Summary: OCI network stack
License: Apache-2.0
URL: https://github.com/containers/netavark/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: rust
Requires: podman

%description
Netavark is a rust based network stack for containers. It is being
designed to work with Podman but is also applicable for other OCI
container management applications.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
cargo build --release

%install
install -Dpm755 -d %{buildroot}%{_libexecdir}/podman
install -Dpm755 -t %{buildroot}%{_libexecdir}/podman target/release/netavark

%files
%license LICENSE
%dir %{_libexecdir}/podman
%{_libexecdir}/podman/netavark

%changelog
