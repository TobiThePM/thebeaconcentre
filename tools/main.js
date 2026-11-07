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

  // booking form -> WhatsApp or email (no data is stored by this site)
  var f=d.getElementById("enquiry");
  if(f){
    function msg(){
      var v=function(n){var el=f.elements[n];return el?el.value.trim():""};
      var lines=["Hello, I'd like to book a session at The Beacon Centre."];
      if(v("name")) lines.push("Name: "+v("name"));
      if(v("service")) lines.push("I'm interested in: "+v("service"));
      if(v("when")) lines.push("Best times for me: "+v("when"));
      if(v("note")) lines.push("What's bringing me here: "+v("note"));
      return lines.join("\n");
    }
    function ok(){ if(!f.elements.name.value.trim()){ f.elements.name.focus(); f.reportValidity&&f.reportValidity(); return false;} return true; }
    d.getElementById("send-wa").addEventListener("click",function(){
      if(!ok()) return;
      window.open("https://wa.me/"+WA+"?text="+encodeURIComponent(msg()),"_blank","noopener");
    });
    d.getElementById("send-mail").addEventListener("click",function(){
      if(!ok()) return;
      var body=msg()+(f.elements.email.value?"\nMy email: "+f.elements.email.value.trim():"");
      window.location.href="mailto:"+EMAIL+"?subject="+encodeURIComponent("Session enquiry")+"&body="+encodeURIComponent(body);
    });
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
