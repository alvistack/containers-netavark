# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: podman-netavark
Epoch: 100
Version: 1.14.0
Release: 1%{?dist}
Summary: OCI network stack
License: Apache-2.0
URL: https://github.com/containers/netavark/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: protobuf-devel
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
