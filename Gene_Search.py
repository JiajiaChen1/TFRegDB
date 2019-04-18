#!/usr/bin/python
import cgi
import cgitb
import subprocess

cgitb.enable()

print("Content-type:text/html")
form = cgi.FieldStorage()
query = form.getvalue("genesearch")
if query == None:
    query = ""
print("""

<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>TFRegDB</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link href="/tfregdb/style.css" rel="stylesheet" type="text/css" />
<script type="text/javascript" src="js/cufon-yui.js"></script>
<script type="text/javascript" src="js/arial.js"></script>
<script type="text/javascript" src="js/cuf_run.js"></script>
</head>
<body>
<div class="main">
  <div class="header">
    <div class="header_resize">
      <div class="nav_menu">
        <ul>
          <li><a href="/tfregdb/index.html">Home</a></li>
          <li class="active"><a href="/cgi-bin/tfregdb/Gene_Search.py">Gene Search</a></li> 
          <li><a href="/cgi-bin/tfregdb/BLAST.py">BLAST Search</a></li> <!--extra work here -->
          <li><a href="/tfregdb/support.html">Support</a></li> <!--extra work here -->
          <li><a href="/tfregdb/about.html">About</a></li> <!--extra work here -->
        </ul>
      </div>
      <div class="clr"></div>
      <div class="logo">
        <h1><a href="index.html">TFRegDB<small>Transcription Factor Regulatory Domain Database</small></a></h1>
      </div>
    </div>
  </div>
  <div class="content">
    <div class="content_resize">
      <div class="mainbar">
        <div class="article">
          <h2>Gene Search</h2>
          <p>Although the name of this search engine is gene search, you can search for a specific protein by entering ENSEMBL transcript id and Uniprot ID.</p>
          <p>Input your HGNC Official Gene Symbol/Ensembl Gene ID/ENSEMBL Transcript ID/Uniprot ID to search for one gene or one isoform of one gene</p>
          <form action='Gene_Search.py' method="post" id="GeneSearch">
            <div><textarea name="genesearch" form="genesearch" style="text-transform: uppercase; font-family: courier; height: 50px; width: 300px;"></textarea></div>
            <div><input type="submit" style="width: 80;" value="Search"/></div>
          </form>
          <div class="result">
            <h2>Result</h2>
            <p>%s</p>
          </div>
          
          <!-- HERE TO PUT RESULTS -->
          
          
        </div>
      </div>
      <div class="sidebar">
        <div class="gadget">
          <h2 class="star">External Links</h2>
          <ul class="sb_menu">
            <li><a href="https://blast.ncbi.nlm.nih.gov/Blast.cgi" target = '_blank'>BLAST</a></li>
            <li><a href="https://www.uniprot.org/" target = '_blank'>Uniprot</a></li>
            <li><a href="https://ensembl.org" target = '_blank'>ENSEMBL Genome Browser</a></li>
          </ul>
        </div>
        <div class="gadget">
          <h2 class="star">Sponsors</h2>
          <ul class="ex_menu">
            <li><a href="https://www.bu.edu/biology/people/profiles/gary-benson/" target="_blank">Gary Benson</a><br />
              Associate Professor of Biology and Computer Science; Program in Bioinformatics, Boston University</li>
            <li><a href="https://www.bu.edu/biology/people/profiles/juan-fuxman-bass/" target="_blank">Juan Fuxman Bass</a><br />
              Assistant Professor, Department of Biology, Boston University</li>
          </ul>
           
            


	   <h2 class="star">Citation</h2>
		<ul class="ex_menu">
            <li><a href="https://www.bu.edu/biology/people/profiles/gary-benson/" target="_blank">Publication</a><br />
              If you use TFRegDB in your work, please cite our publication here.</li>

	  </ul>
     <h2 class="star">Let us see how popular we are</h2>
     <ul><script type="text/javascript" src="//ra.revolvermaps.com/0/0/6.js?i=01zha4fqte8&amp;m=7&amp;c=e63100&amp;cr1=ffffff&amp;f=arial&amp;l=0&amp;bv=90&amp;lx=-420&amp;ly=420&amp;hi=20&amp;he=7&amp;hc=a8ddff&amp;rs=80" async="async"></script></ul>
        </div>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="fbg">
    <div class="fbg_resize">
      <div class="col c1">
        <div class="clr"></div>
        <h2>Softwares and Database</h2>
        <p><a href='https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=Download',target='_blank'>BLAST+</a></p>
        <p><a href='https://www.ncbi.nlm.nih.gov/protein',target='_blank'>NCBI Human Protein Database</a></p>
        <p><a href='http://jmol.sourceforge.net/',target='_blank'>Jmol: an open-source browser-based HTML5 viewer and stand-alone Java viewer for chemical structures in 3D</a></p>
      </div>
      <div class="col c2">
        <h2>Features of TFRegDB</h2>
        <p>Coming Soon </p>
        
      </div>
      <div class="col c3">
        <h2>Contact</h2>
        <p>Juan Fuxman Bass</p>
        <p>Assistant Professor, Department of Biology, Boston University</p>
        <strong>E-mail:</strong> <a href="fuxman@bu.edu">fuxman@bu.edu</a></p>
        <p>Zhaorong Li</p>
        <p>Graduate Student in Bioinformatics Program, Boston University</p>
        <strong>E-mail:</strong> <a href="zhaorong@bu.edu">zhaorong@bu.edu</a></p>
      </div>
      <div class="clr"></div>
    </div>
  </div>
  <div class="footer">
    <div class="footer_resize">
      <p class="lf">&copy; Copyright MyWebSite. Designed by Blue <a href="http://www.bluewebtemplates.com/">Website Templates</a></p>
      <ul class="fmenu">
       <!-- <li class="active"><a href="index.html">Home</a></li>
        <li><a href="index.html">Gene Search</a></li>
        <li><a href="index.html">BLAST Search</a></li>
        <li><a href="index.html">Support</a></li>" --> 
      </ul>
    </div>
    <div class="clr"></div>
  </div>
</div>
</body>
</html>
""" % ((query))