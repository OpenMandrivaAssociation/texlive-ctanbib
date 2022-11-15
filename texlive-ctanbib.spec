Name:		texlive-ctanbib
Version:	59782
Release:	1
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
%{_texmfdistdir}/texmf-dist/scripts/ctanbib
%doc %{_texmfdistdir}/texmf-dist/doc/support/ctanbib
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ctanbib.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/ctanbib.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
