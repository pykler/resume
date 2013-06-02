#!/bin/bash

public_files=(hatem-nassrat-resume.html hatem-nassrat-resume.pdf hatem-nassrat-resume-small-public.html)
private_files=(hatem_nassrat.doc hatem_nassrat.html hatem_nassrat.odt hatem_nassrat.pdf hatem_nassrat.tex)

echo Nassrat.ca
scp ${private_files[@]} nassrat@nassrat.ca:nassrat.ca/resume/
scp ${public_files[@]} nassrat@nassrat.ca:nassrat.ca/
echo Torch
scp ${public_files[@]} nassrat@bluenose.cs.dal.ca:public_html/
