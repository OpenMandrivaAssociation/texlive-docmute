Name:		texlive-docmute
Version:	25741
Release:	1
Summary:	Input files ignoring LaTeX preamble, etc
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/docmute
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docmute.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Input or include stand-alone LaTeX documents, ignoring
everything but the material between \begin{document} and
\end{document}.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/docmute/docmute.sty
%doc %{_texmfdistdir}/doc/latex/docmute/README
%doc %{_texmfdistdir}/doc/latex/docmute/docmute.pdf
#- source
%doc %{_texmfdistdir}/source/latex/docmute/docmute.dtx
%doc %{_texmfdistdir}/source/latex/docmute/docmute.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
