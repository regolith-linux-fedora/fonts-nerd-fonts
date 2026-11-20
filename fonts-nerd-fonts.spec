Name:           fonts-nerd-fonts
Version:        3.5.1
Release:        1%{?dist}
URL:            https://github.com/regolith-linux/fonts-nerd-fonts
# The repository holds every family's fonts, too much for a source RPM, so
# Source0 holds only the paths this spec packages (voulage spec style guide,
# "Large repositories"). More families become more blocks below.
%global source0_paths usr/share/fonts/truetype/bitstreamverasansmono usr/share/fontconfig/conf.avail/30-fonts-nerd-font-bitstreamverasansmono.conf debian/copyright
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# The repository has no licence texts besides debian/copyright (MIT); these
# come from the Nerd Fonts release the fonts were taken from.
Source1:        https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%{version}/LICENSE#/nerd-fonts-LICENSE
Source2:        https://raw.githubusercontent.com/ryanoasis/nerd-fonts/v%{version}/patched-fonts/BitstreamVeraSansMono/Bitstream%20Vera%20License.txt#/Bitstream-Vera-License.txt

# The base font is Bitstream Vera; the added glyph sets are MIT, OFL-1.1,
# Apache-2.0 (Material Design), CC-BY-4.0 (Font Awesome icons, Codicons) and
# Unlicense (Font Logos), per Nerd Fonts' license-audit.md.
%global fontlicense       Bitstream-Vera AND MIT AND OFL-1.1 AND Apache-2.0 AND CC-BY-4.0 AND Unlicense
%global fontlicenses      nerd-fonts-LICENSE Bitstream-Vera-License.txt debian/copyright

# Nerd Fonts 3 renamed "BitstreamVeraSansMono Nerd Font" to "BitstromWera
# Nerd Font", as the Bitstream Vera licence requires of modified versions.
# Upstream's fontconfig file maps the old names, which Regolith's looks use,
# to the new ones.
%global fontfamily0       BitstromWera Nerd Font
%global fontpkgname0      bitstromwera-nerd-fonts
%global fontsummary0      Fixed-width font with the Nerd Fonts icons, for Regolith
%global fonts0            usr/share/fonts/truetype/bitstreamverasansmono/*.ttf
%global fontconfs0        usr/share/fontconfig/conf.avail/30-fonts-nerd-font-bitstreamverasansmono.conf
%global fontpkgheader0    %{expand:
Provides:       fonts-nerd-font-bitstreamverasansmono = %{version}-%{release}
}
%global fontdescription0  %{expand:
The Nerd Fonts build of a classic fixed-width font, renamed as its license
requires, with several thousand icons added for status bars, prompts and
editors. It comes in two variants: one with wide icons and one where every
glyph has the same width. The default Regolith look uses it.}

Summary:        Nerd Fonts families used by Regolith
License:        %{fontlicense}
BuildArch:      noarch

%description
Nerd Fonts families used by Regolith, one package per family.

%fontpkg -a -s

%prep
%autosetup
cp -p %{SOURCE1} %{SOURCE2} .

%build
%fontbuild -a

%install
%fontinstall -a

%check
%fontcheck -a

%fontfiles -a

%changelog
* Wed Nov 18 2026 Regolith Fedora Port <port@regolith.invalid> - 3.5.1-1
- Initial package
