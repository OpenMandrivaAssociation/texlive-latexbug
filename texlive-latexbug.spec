Name:		texlive-latexbug
Version:	72762
Release:	1
Summary:	Bug-classification for LaTeX related bugs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latexbug
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbug.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbug.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexbug.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is written in order to help identifying the
rightful addressee for a bug report. The LaTeX team asks that
it will be loaded in any test file that is intended to be sent
to the LaTeX bug database as part of a bug report.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/latexbug
%{_texmfdistdir}/tex/latex/latexbug
%doc %{_texmfdistdir}/doc/latex/latexbug

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
