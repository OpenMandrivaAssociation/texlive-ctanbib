Name:		texlive-ctanbib
Version:	59782
Release:	2
Summary:	Export CTAN entries to bib format
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ctanbib
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanbib.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a Lua script which can be used for
retrieving bibliographic information in BibLaTeX format for
packages hosted on CTAN. The ctanbib script depends only on
LuaXML.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/scripts/ctanbib
%doc %{_texmfdistdir}/doc/support/ctanbib
%doc %{_texmfdistdir}/doc/man/man1/*

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
