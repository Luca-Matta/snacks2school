import{d as _,r as o,C as z,o as B,g as D,t as E,H as F,A as b,z as k,x as s,y as M,S as j,T as l,U as c,V as C,O as h,B as w,I as T,J as H,K as L}from"./Lh55aVSo.js";import{_ as $}from"./inWKtfgP.js";import{a as x}from"./upsvKRUO.js";import{a as N}from"./C_D2JwHD.js";const A={class:"flex justify-center items-center bg-[#f5f5f5] h-full pb-16"},X={class:"flex flex-col justify-center items-center"},q={class:"bg-white !rounded-3xl shadow-card w-[335px] md:w-auto md:min-w-96 p-6 mt-6 md:mt-12"},J={class:"text-sm opacity-80 mt-2"},K={class:"mb-3"},O={class:"mb-3"},G={class:"mb-3"},Q={class:"mb-3"},W={class:"mb-3 relative"},Y=["type"],Z={class:"mb-3 relative"},ee=["type"],se={class:"text-sm mt-3 mb-0 text-lead"},ie=_({__name:"signup-customer",setup(te){const n=o("password"),p=o(""),d=o(""),m=o(""),f=o("");o(""),o(""),o("");const i=o(""),u=o(""),S=o([]);o(null),o([]),o(null),o([]);const v=z().query.ref||"",g=()=>{n.value=n.value==="password"?"text":"password"},U=async()=>(await x.get("https://www.snacks2school.com/api/csrf-token/",{withCredentials:!0})).data.csrfToken,y=o(0),V=async()=>{try{const t=await fetch("https://www.snacks2school.com/api/user-count/");if(!t.ok)throw new Error(`HTTP error! status: ${t.status}`);const e=await t.json();y.value=e.user_count}catch(t){console.error("Error fetching user count:",t)}},P=async()=>{try{const t=await x.get("https://www.snacks2school.com/api/provinces/");S.value=t.data}catch(t){console.error("Error fetching provinces:",t)}},R=async()=>{try{const e=(await N.get("csrf-token/")).data.csrfToken,r=await N.post("login/",{username:d.value,password:i.value},{headers:{"X-CSRFToken":e},withCredentials:!0});r.data.token&&(localStorage.setItem("authToken",r.data.token),window.location.href="/")}catch(t){console.error("Login failed:",t)}},I=async()=>{try{if(i.value!==u.value){console.error("Passwords do not match");return}const t=await U(),e={email:p.value,username:d.value,first_name:m.value,last_name:f.value,password:i.value,confirm_password:u.value};let r="https://www.snacks2school.com/api/signup/customer/";v&&(r+=`?ref=${v}`);const a=await x.post(r,e,{headers:{"X-CSRFToken":t},withCredentials:!0});a.data.token?(document.cookie=`token=${a.data.token}`,await R()):console.error("No token received")}catch(t){console.error("Signup failed:",t)}};return B(()=>{V(),P()}),(t,e)=>{const r=D("router-link");return E(),F(T(L),null,{default:b(()=>[k(T(H),{fullscreen:!0},{default:b(()=>[s("div",A,[s("div",X,[e[18]||(e[18]=s("img",{src:$,alt:"star",class:"h-32 w-32"},null,-1)),e[19]||(e[19]=s("div",{class:"text-4xl md:text-5xl font-bold"},"Snacks2School",-1)),e[20]||(e[20]=s("p",{class:"max-w-96 text-center !py-4"},"La merenda a portata di clic",-1)),s("div",q,[e[16]||(e[16]=s("div",{class:"text-2xl font-semibold !text-black"},"Registrati",-1)),s("p",J," Unisciti ai "+M(y.value)+" utenti di Snacks2School ",1),e[17]||(e[17]=s("hr",{class:"mt-6 mb-4"},null,-1)),s("form",{class:"mb-3",onSubmit:j(I,["prevent"])},[s("div",K,[e[6]||(e[6]=s("label",{class:"block text-xs mb-1"},"Email *",-1)),l(s("input",{"onUpdate:modelValue":e[0]||(e[0]=a=>p.value=a),id:"email",name:"email",type:"text",class:"w-full bg-[#f5f5f5] border border-[#e0e0e0]",style:{"border-radius":"5px",padding:"7px"}},null,512),[[c,p.value]])]),s("div",O,[e[7]||(e[7]=s("label",{class:"block text-xs mb-1"},"Nome utente *",-1)),l(s("input",{"onUpdate:modelValue":e[1]||(e[1]=a=>d.value=a),id:"username",name:"username",type:"text",class:"w-full bg-[#f5f5f5] border border-[#e0e0e0]",style:{"border-radius":"5px",padding:"7px"}},null,512),[[c,d.value]])]),s("div",G,[e[8]||(e[8]=s("label",{class:"block text-xs mb-1"},"Nome genitore *",-1)),l(s("input",{"onUpdate:modelValue":e[2]||(e[2]=a=>m.value=a),id:"firstName",name:"firstName",type:"text",class:"w-full bg-[#f5f5f5] border border-[#e0e0e0]",style:{"border-radius":"5px",padding:"7px"}},null,512),[[c,m.value]])]),s("div",Q,[e[9]||(e[9]=s("label",{class:"block text-xs mb-1"},"Cognome genitore *",-1)),l(s("input",{"onUpdate:modelValue":e[3]||(e[3]=a=>f.value=a),id:"lastName",name:"lastName",type:"text",class:"w-full bg-[#f5f5f5] border border-[#e0e0e0]",style:{"border-radius":"5px",padding:"7px"}},null,512),[[c,f.value]])]),s("div",W,[e[10]||(e[10]=s("label",{class:"block text-xs mb-1"},"Password *",-1)),l(s("input",{"onUpdate:modelValue":e[4]||(e[4]=a=>i.value=a),id:"password",name:"password",type:n.value,class:"w-full bg-[#f5f5f5] border border-[#e0e0e0]",style:{"border-radius":"5px",padding:"7px"}},null,8,Y),[[C,i.value]]),s("i",{class:h([n.value==="password"?"fas fa-eye":"fas fa-eye-slash","absolute right-3 top-10 transform -translate-y-1/2 cursor-pointer"]),onClick:g},null,2)]),s("div",Z,[e[11]||(e[11]=s("label",{class:"block text-xs mb-1"},"Conferma password *",-1)),l(s("input",{"onUpdate:modelValue":e[5]||(e[5]=a=>u.value=a),id:"confirmPassword",name:"confirmPassword",type:n.value,class:"w-full bg-[#f5f5f5] border border-[#e0e0e0]",style:{"border-radius":"5px",padding:"7px"}},null,8,ee),[[C,u.value]]),s("i",{class:h([n.value==="password"?"fas fa-eye":"fas fa-eye-slash","absolute right-3 top-10 transform -translate-y-1/2 cursor-pointer"]),onClick:g},null,2)]),e[14]||(e[14]=s("div",{class:"text-left"},[s("label",{class:"text-gray-[#888] text-xs",for:"flexCheckDefault"},[w(' Facendo clic su "Registrati" accetti i nostri '),s("a",{href:"",class:"iubenda-nostyle iubenda-noiframe iubenda-embed iubenda-noiframe underline !text-[#888]",title:"Termini e Condizioni"}," Termini e condizioni ")])],-1)),e[15]||(e[15]=s("div",{class:"text-center"},[s("button",{type:"submit",class:"btn bg-[#ffa500] w-full font-bold uppercase text-xs shadow-button my-4 mb-2 !py-3 !px-6 !rounded-lg"}," Registrati ")],-1)),s("p",se,[e[13]||(e[13]=w(" Hai già un account? ")),k(r,{to:"/login",class:"font-bold !text-black"},{default:b(()=>e[12]||(e[12]=[w("Accedi")])),_:1})])],32)])])])]),_:1})]),_:1})}}});export{ie as default};
