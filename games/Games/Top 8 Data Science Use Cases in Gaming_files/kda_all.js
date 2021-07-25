function kda_top () {
var path=kpath + 'aps/';
var ts=new Date().getTime();
var ms=new Date().getMilliseconds();
var Top_nam=new Array(); var Top_ext=new Array(); var Top_wid=new Array(); var Top_hgt=new Array();
var Top_alt=new Array(); var Top_txt=new Array(); var Top_url=new Array(); var Top_wgt=new Array(); var wgt=0;
wgt+=1; Top_wgt[1]=wgt;
Top_nam[1]="t-drb-20m10-humai"; Top_ext[1]=".jpg"; Top_wid[1]=750; Top_hgt[1]=100;
Top_url[1]='https://www.datarobot.com/resource/humility-in-ai/?utm_source=KDN&utm_medium=3rdpartypromoter&utm_campaign=20Humility-KDNb';
Top_txt[1]="Humility in AI: Building Trustworthy and Ethical AI Systems";
Top_alt[1]="txt";
wgt+=1; Top_wgt[2]=wgt;
Top_nam[2]="t-sas-20m11-learn"; Top_ext[2]=".gif"; Top_wid[2]=1; Top_hgt[2]=1;
Top_url[2]='<ins class="dcmads" style="display:inline-block;width:750px;height:100px" data-dcm-placement="N6626.289580.KDNUGGETS.COM/B23482495.282859034" data-dcm-rendering-mode="iframe" data-dcm-https-only data-dcm-resettable-device-id="" data-dcm-app-id=""> <script src="https://www.googletagservices.com/dcm/dcmads.js"></script></ins>';
Top_txt[2]="Talent Development Plan? SAS can help";
Top_alt[2]="txt";
wgt+=1; Top_wgt[3]=wgt;
Top_nam[3]="t-jmp-20m11-trial"; Top_ext[3]=".jpg"; Top_wid[3]=750; Top_hgt[3]=100;
Top_url[3]='https://www.jmp.com/en_us/download-jmp-free-trial.html?utm_source=kdnuggetswc&utm_medium=advertisement&utm_campaign=td7013Z000002sEGsQAM&utm_content=thirdparty';
Top_txt[3]="See what you can discover with powerful stats and interactive visualization. Try JMP Free Trial &gt;";
Top_alt[3]="JMP";
wgt+=1; Top_wgt[4]=wgt;
Top_nam[4]="t-imm-20m10-7steps"; Top_ext[4]=".jpg"; Top_wid[4]=750; Top_hgt[4]=100;
Top_url[4]='https://www.immuta.com/seven-steps-for-migrating-sensitive-data-to-the-cloud-a-guide-for-data-teams/?utm_medium=Paid&utm_source=Paid-KDnuggets&utm_term=DB_KDnuggets&utm_campaign=NA-Prospecting-Display-DB_KDnuggets-WP_Cloud_Migration_Checklist-Paid-KDnuggets';
Top_txt[4]="7 Steps for Migrating Sensitive Data to the Cloud - A Guide for Data Teams. Download Now";
Top_alt[4]="txt";
var rtop=Math.random()*4;
var n_ad=1; while (Top_wgt[n_ad]<rtop) {n_ad++};
var out='<table border=0 cellspacing=5 cellpadding=20 width=990><tr><td valign=top align=center width=750>';
  var whb=' width="90%" border=0';
  if (Top_wid[n_ad] == 1) {
      out+=Top_url[n_ad];
      whb=' width=1 height=1';
  } else {
      out+='<a href=' + Top_url[n_ad] + ' onclick="ga(\'send\',\'pageview\',\'/zt/' + Top_nam[n_ad] + '\');" target=_blank>';
  }
  out+='<img src=' + path + Top_nam[n_ad] + Top_ext[n_ad] + '?ms=' + ms + whb + ' alt="' + Top_alt[n_ad] + '">';
  out+='<br><b><font size="+1">' + Top_txt[n_ad] + '</font></b></a></td>';
  out+='</tr></table><br>';document.writeln(out);}
function kda_sid_init() {
var ts=new Date().getTime();
Sid_nam=new Array(); Sid_ext=new Array(); Sid_txt=new Array(); Sid_url=new Array();
Sid_alt=new Array(); Sid_wid=new Array(); Sid_hgt=new Array(); Sid_wgt=new Array(); var wgt=0;
wgt+=1; Sid_wgt[1]=wgt;
Sid_nam[1]="e-sas-20m06"; Sid_ext[1]=".gif"; Sid_wid[1]=1; Sid_hgt[1]=1;
Sid_url[1]='<ins class="dcmads" style="display:inline-block;width:300px;height:250px" data-dcm-placement="N6626.289580.KDNUGGETS.COM/B23482492.275730892" data-dcm-rendering-mode="iframe" data-dcm-https-only data-dcm-resettable-device-id="" data-dcm-app-id=""> <script src="https://www.googletagservices.com/dcm/dcmads.js"></script></ins>';
Sid_txt[1]="SAS Viya<br>";
Sid_alt[1]="SAS";
wgt+=2; Sid_wgt[2]=wgt;
Sid_nam[2]="e-kni-20m12a-43"; Sid_ext[2]=".png"; Sid_wid[2]=300; Sid_hgt[2]=250;
Sid_url[2]='https://www.knime.com/whats-new-in-knime-43?utm_source=kdnuggets&utm_medium=display&utm_term=whats-new&utm_content=article&utm_campaign=Release-202012';
Sid_txt[2]="KNIME Analytics Platform 4.3<br>and KNIME Server 4.12<br>Download Now";
Sid_alt[2]="KNIME Analytics Platform 4.3 and KNIME Server 4.12<br>Download Now";
wgt+=1; Sid_wgt[3]=wgt;
Sid_nam[3]="e-imm-20m10-7steps"; Sid_ext[3]=".jpg"; Sid_wid[3]=300; Sid_hgt[3]=250;
Sid_url[3]='https://www.immuta.com/seven-steps-for-migrating-sensitive-data-to-the-cloud-a-guide-for-data-teams/?utm_medium=Paid&utm_source=Paid-KDnuggets&utm_term=DB_KDnuggets&utm_campaign=NA-Prospecting-Display-DB_KDnuggets-WP_Cloud_Migration_Checklist-Paid-KDnuggets';
Sid_txt[3]="Immuta<br>7 Steps for<br>Migrating Sensitive Data<br>to the Cloud<br>A Guide for Data Teams<br>Download Now";
Sid_alt[3]="Immuta 7 Steps for<br>Migrating Sensitive Data<br>to the Cloud<br>A Guide for Data Teams<br>Download Now";
}
function kda_sid_write (nads) {
  if (nads != 0) {nads=1};
  var path=kpath + 'aps/';
  var ms=new Date().getMilliseconds(); var adshown=new Array();
  for (adpos=1; adpos<=nads; adpos++) {
    do { var adn=1; var re=Math.random()*4;
      while (Sid_wgt[adn]<re) {adn++};
    } while (adshown[adn]==1);
    if (Sid_wid[adn]==1) { s=Sid_url[adn]; s=s.replace('ze/e-','ze/' + nads + adpos + ':e-'); 
      s+='<img src=' + path + Sid_nam[adn] + '.gif?ms' + ms + ' width=1 height=1 border=0>';
    } else {
      s='<a href=' + Sid_url[adn] + ' onclick="ga(\'send\',\'pageview\',\'/ze/' + nads + adpos + ':' + Sid_nam[adn] + '\');" target=_blank>';
      s+='<img src=' + path + Sid_nam[adn] + Sid_ext[adn] + '?ms' + ms +  ' width=' + Sid_wid[adn] + ' height=' + Sid_hgt[adn] + ' border=0 alt="' + Sid_alt[adn] + '">';}
    s+='<br><b>' + Sid_txt[adn] + '</b></a><br><br>';
    if (nads>1) {s+='<br><hr class="grey-line"><br>'};
    document.writeln(s); adshown[adn]=1;
  }
}
