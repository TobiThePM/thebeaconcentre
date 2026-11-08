(function(){
  var WA="2348181057549", EMAIL="beaconwellnesscentre@gmail.com";
  var d=document, root=d.documentElement;

  // header state + mobile menu
  var head=d.querySelector(".site-head"), nav=d.getElementById("nav"), mb=d.querySelector(".menu-btn");
  function onScroll(){ head&&head.classList.toggle("scrolled",window.scrollY>10); }
  onScroll(); window.addEventListener("scroll",onScroll,{passive:true});
  if(mb&&nav){
    mb.addEventListener("click",function(){
      var o=nav.classList.toggle("open"); mb.setAttribute("aria-expanded",o); mb.textContent=o?"Close":"Menu";
    });
    nav.addEventListener("click",function(e){ if(e.target.tagName==="A"){ nav.classList.remove("open"); mb.textContent="Menu"; mb.setAttribute("aria-expanded","false"); }});
  }

  // beacon glow follows the pointer on the hero
  var hero=d.querySelector(".hero");
  if(hero && window.matchMedia("(pointer:fine)").matches && !window.matchMedia("(prefers-reduced-motion:reduce)").matches){
    var raf=0;
    hero.addEventListener("pointermove",function(e){
      if(raf) return;
      raf=requestAnimationFrame(function(){
        var r=hero.getBoundingClientRect();
        hero.style.setProperty("--mx",((e.clientX-r.left)/r.width*100).toFixed(1)+"%");
        hero.style.setProperty("--my",((e.clientY-r.top)/r.height*100).toFixed(1)+"%");
        raf=0;
      });
    });
  }

  // reveal on scroll
  var items=d.querySelectorAll(".rv");
  if("IntersectionObserver" in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target);} });
    },{threshold:.12,rootMargin:"0px 0px -6% 0px"});
    items.forEach(function(el){io.observe(el)});
  } else items.forEach(function(el){el.classList.add("in")});

  var PH={"":"book a session (I'm not sure which service is right for me yet)","individual":"book an individual counselling session","couples":"book a couples counselling session",
      "groups":"find out about your group therapy and support","corporate":"talk to you about corporate mental health and workplace wellness support",
      "workshops":"enquire about a workshop, training or masterclass","programmes":"find out about your specialised healing programmes","speaking":"enquire about speaking or facilitation"};

  // booking form -> WhatsApp or email (no data is stored by this site)
  var f=d.getElementById("enquiry");
  if(f){
    function msg(){
      var v=function(n){var el=f.elements[n];return el?el.value.trim():""};
      var k=v("service"), lines=["Hello, I just checked your website. My name is "+v("name")+" and I'd like to "+(PH[k]||PH[""])+"."];
      if(v("when")) lines.push("Best times for me: "+v("when"));
      if(v("note")) lines.push("What's bringing me here: "+v("note"));
      return lines.join("\n");
    }
    function ok(){ if(!f.elements.name.value.trim()){ f.elements.name.focus(); f.reportValidity&&f.reportValidity(); return false;} return true; }
    d.getElementById("send-wa").addEventListener("click",function(){
      if(!ok()) return;
      window.open("https://wa.me/"+WA+"?text="+encodeURIComponent(msg()),"_blank","noopener");
    });
    var help=d.getElementById("mail-help");
    d.getElementById("send-mail").addEventListener("click",function(){
      if(!ok()) return;
      var body=msg()+(f.elements.email.value?"\nMy email: "+f.elements.email.value.trim():"");
      var sub="Session enquiry";
      var q="subject="+encodeURIComponent(sub)+"&body="+encodeURIComponent(body);
      d.getElementById("m-gmail").href="https://mail.google.com/mail/?view=cm&fs=1&to="+EMAIL+"&su="+encodeURIComponent(sub)+"&body="+encodeURIComponent(body);
      d.getElementById("m-app").href="mailto:"+EMAIL+"?"+q;
      d.getElementById("m-copy").onclick=function(){
        var note=d.getElementById("m-note"), text="To: "+EMAIL+"\nSubject: "+sub+"\n\n"+body;
        function done(){ note.textContent="Copied. Paste it into a new email to "+EMAIL+"."; }
        if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(text).then(done,function(){ note.textContent="Please copy the message manually and send it to "+EMAIL+"."; }); }
        else { note.textContent="Please copy the message manually and send it to "+EMAIL+"."; }
      };
      help.hidden=false; help.scrollIntoView({behavior:"smooth",block:"nearest"});
    });
  }



  // service buttons: ask for a name, then open WhatsApp with a message written for that service
  var waLinks=d.querySelectorAll("a[data-wa]");
  if(waLinks.length){
    var key="", box=d.createElement("div");
    box.className="wa-pop"; box.hidden=true;
    box.innerHTML='<div class="wa-pop-card" role="dialog" aria-modal="true" aria-labelledby="wa-t"><button type="button" class="wa-pop-x" aria-label="Close">&times;</button>'+
      '<h3 id="wa-t">Nearly there</h3><p class="wa-pop-pick" id="wa-p" hidden></p><p class="wa-pop-sub" id="wa-s"></p>'+
      '<form id="wa-f"><label for="wa-n">Your name</label><input id="wa-n" autocomplete="name" placeholder="How should we address you?" required>'+
      '<label for="wa-w">When suits you best? (optional)</label><input id="wa-w" placeholder="e.g. weekday evenings">'+
      '<button class="btn" type="submit">Continue to WhatsApp <span class="arr" aria-hidden="true">→</span></button></form>'+
      '<p class="wa-pop-skip"><a href="#" id="wa-skip">Skip and write my name in WhatsApp</a></p></div>';
    d.body.appendChild(box);
    var nm=box.querySelector("#wa-n"), sub=box.querySelector("#wa-s"), last=null;
    var pkg="", price="", pk=box.querySelector("#wa-p"), when=box.querySelector("#wa-w");
    function openPop(k,from){
      nm.value=""; when.value=""; key=PH.hasOwnProperty(k)?k:""; last=from; pkg=from.getAttribute("data-pkg")||""; price=from.getAttribute("data-price")||"";
      if(pkg){ pk.textContent="Your choice: "+(from.parentNode.querySelector("span")||{}).textContent+" · "+price; pk.hidden=false; sub.textContent="We’ll open WhatsApp with your choice and your name already written, so we can reply with times and next steps."; }
      else { pk.hidden=true; sub.textContent="We’ll open WhatsApp with a message already written for you: “"+PH[key]+"”."; }
      box.hidden=false; d.body.classList.add("wa-open"); setTimeout(function(){nm.focus()},30);
    }
    function closePop(){ box.hidden=true; d.body.classList.remove("wa-open"); if(last) last.focus(); }
    var FOR={"individual":"individual counselling","couples":"couples counselling"};
    function go(name){
      var who=name||"______", w=when.value.trim(), m;
      if(pkg){
        m="Hello, I just checked your website. My name is "+who+" and I'd like to book "+pkg+" for "+FOR[key]+" ("+price+")."+(w?" Best times for me: "+w+".":"")+" Please could you let me know the available times and how to confirm my slot?";
      } else {
        var tail=(key===""||key==="individual"||key==="couples")?" Please could you let me know the available times and the next step?":" Please could you share more details and the next step?";
        m="Hello, I just checked your website. My name is "+who+" and I'd like to "+PH[key]+"."+(w?" Best times for me: "+w+".":"")+tail;
      }
      window.open("https://wa.me/"+WA+"?text="+encodeURIComponent(m),"_blank","noopener");
      closePop();
    }
    waLinks.forEach(function(a){ a.addEventListener("click",function(e){ e.preventDefault(); openPop(a.getAttribute("data-wa")||"",a); }); });
    box.querySelector("#wa-f").addEventListener("submit",function(e){ e.preventDefault(); go(nm.value.trim()); });
    box.querySelector("#wa-skip").addEventListener("click",function(e){ e.preventDefault(); go(""); });
    box.querySelector(".wa-pop-x").addEventListener("click",closePop);
    box.addEventListener("click",function(e){ if(e.target===box) closePop(); });
    d.addEventListener("keydown",function(e){ if(e.key==="Escape"&&!box.hidden) closePop(); });
  }

  // resources sign-up (opens an email to the centre until a mailing list is connected)
  var s=d.getElementById("signup");
  if(s){
    s.addEventListener("submit",function(e){
      e.preventDefault();
      var em=s.elements.email.value.trim();
      if(!s.elements.consent.checked){ s.elements.consent.focus(); return; }
      window.location.href="mailto:"+EMAIL+"?subject="+encodeURIComponent("Keep me posted")+"&body="+encodeURIComponent("Please add me to your updates list: "+em);
    });
  }
  var y=d.getElementById("yr"); if(y) y.textContent=new Date().getFullYear();
})();
