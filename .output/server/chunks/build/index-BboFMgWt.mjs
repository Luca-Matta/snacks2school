import { a as buildAssetsURL } from '../routes/renderer.mjs';
import { useSSRContext, mergeProps } from 'vue';
import { ssrRenderAttrs, ssrRenderComponent, ssrRenderAttr } from 'vue/server-renderer';
import { _ as _export_sfc } from './server.mjs';
import 'vue-bundle-renderer/runtime';
import '../runtime.mjs';
import 'node:http';
import 'node:https';
import 'node:fs';
import 'node:path';
import 'node:url';
import 'devalue';
import '@unhead/ssr';
import 'unhead';
import '@unhead/shared';
import 'vue-router';

const _sfc_main$1 = {};
function _sfc_ssrRender$1(_ctx, _push, _parent, _attrs) {
  _push(`<header${ssrRenderAttrs(mergeProps({ class: "bg-background/75 backdrop-blur-[8px] border-b-[0.5px] border-gray border-opacity-100 sticky top-0 z-50 mb-8" }, _attrs))}><div class="mx-auto px-4 sm:px-6 lg:px-8 max-w-7xl flex items-center justify-between gap-3 h-16"><div class="flex items-center gap-1.5"><a href="" class="flex-shrink-0 font-bold text-xl text-gray-900 dark:text-white flex items-end gap-1.5" aria-label="Home"> Snack2School </a></div><nav class="flex items-center gap-4"><a href="" class="text-gray hover:text-blue-600">About</a><a href="" class="text-gray hover:text-blue-600">Store</a><a href="" class="text-gray hover:text-blue-600">Contatti</a></nav><div class="flex items-center gap-3"><button class="bg-pink text-gray px-4 py-2 rounded-md">Accedi</button><button class="border border-gray text-gray px-4 py-2 rounded-md"> Registrati </button></div></div></header>`);
}
const _sfc_setup$1 = _sfc_main$1.setup;
_sfc_main$1.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("components/Navbar.vue");
  return _sfc_setup$1 ? _sfc_setup$1(props, ctx) : void 0;
};
const __nuxt_component_0 = /* @__PURE__ */ _export_sfc(_sfc_main$1, [["ssrRender", _sfc_ssrRender$1]]);
const _imports_0 = "" + buildAssetsURL("home-header.CrdB4B0T.mp4");
const _imports_1 = "" + buildAssetsURL("panificio_drago.Cc-kiRe5.png");
const _imports_2 = "data:image/svg+xml,%3csvg%20xmlns='http://www.w3.org/2000/svg'%20fill='%23facc15'%20viewBox='0%200%2024%2024'%20stroke='currentColor'%20class='w-6%20h-6'%20%3e%3cpath%20stroke-linecap='round'%20stroke-linejoin='round'%20stroke-width='2'%20d='M12%2017.27L18.18%2021l-1.64-7.03L22%209.24l-7.19-.61L12%202%209.19%208.63%202%209.24l5.46%204.73L5.82%2021z'%20/%3e%3c/svg%3e";
const _sfc_main = {};
function _sfc_ssrRender(_ctx, _push, _parent, _attrs) {
  const _component_Navbar = __nuxt_component_0;
  _push(`<div${ssrRenderAttrs(_attrs)}>`);
  _push(ssrRenderComponent(_component_Navbar, null, null, _parent));
  _push(`<div class="max-w-screen-xl mx-auto pb-8"><video class="w-full h-auto" autoplay muted><source${ssrRenderAttr("src", _imports_0)} type="video/mp4"> Your browser does not support the video tag. </video></div><div class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-16 gap-12"><h2 class="text-4xl font-bold">I MIGLIORI STORE A MASSA</h2><div class="flex flex-wrap justify-center items-center gap-8"><div class="flex flex-col justify-center items-center gap-2"><div class="flex justify-center items-center h-60 w-60 bg-gray rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer"><img${ssrRenderAttr("src", _imports_1)} alt="" class="bg-center bg-contain bg-no-repeat h-52 w-52"></div><div class="flex flex-col justify-center items-center"><div class="flex items-center justify-center gap-1"><p class="font-bold">Panificio Drago</p><img${ssrRenderAttr("src", _imports_2)} alt="star" class="h-6 w-6"></div><p class="text-xs opacity-80">Viale Roma, 365, 54100, Massa (MS)</p></div></div><div class="flex flex-col justify-center items-center gap-2"><div class="flex justify-center items-center h-60 w-60 bg-gray rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer"><img${ssrRenderAttr("src", _imports_1)} alt="" class="bg-center bg-contain bg-no-repeat h-52 w-52"></div><div class="flex flex-col justify-center items-center"><div class="flex items-center justify-center gap-1"><p class="font-bold">Panificio Drago</p><img${ssrRenderAttr("src", _imports_2)} alt="star" class="h-6 w-6"></div><p class="text-xs opacity-80">Viale Roma, 365, 54100, Massa (MS)</p></div></div><div class="flex flex-col justify-center items-center gap-2"><div class="flex justify-center items-center h-60 w-60 bg-gray rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer"><img${ssrRenderAttr("src", _imports_1)} alt="" class="bg-center bg-contain bg-no-repeat h-52 w-52"></div><div class="flex flex-col justify-center items-center"><div class="flex items-center justify-center gap-1"><p class="font-bold">Panificio Drago</p><img${ssrRenderAttr("src", _imports_2)} alt="star" class="h-6 w-6"></div><p class="text-xs opacity-80">Viale Roma, 365, 54100, Massa (MS)</p></div></div><div class="flex flex-col justify-center items-center gap-2"><div class="flex justify-center items-center h-60 w-60 bg-gray rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer"><img${ssrRenderAttr("src", _imports_1)} alt="" class="bg-center bg-contain bg-no-repeat h-52 w-52"></div><div class="flex flex-col justify-center items-center"><div class="flex items-center justify-center gap-1"><p class="font-bold">Panificio Drago</p><img${ssrRenderAttr("src", _imports_2)} alt="star" class="h-6 w-6"></div><p class="text-xs opacity-80">Viale Roma, 365, 54100, Massa (MS)</p></div></div><div class="flex flex-col justify-center items-center gap-2"><div class="flex justify-center items-center h-60 w-60 bg-gray rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer"><img${ssrRenderAttr("src", _imports_1)} alt="" class="bg-center bg-contain bg-no-repeat h-52 w-52"></div><div class="flex flex-col justify-center items-center"><div class="flex items-center justify-center gap-1"><p class="font-bold">Panificio Drago</p><img${ssrRenderAttr("src", _imports_2)} alt="star" class="h-6 w-6"></div><p class="text-xs opacity-80">Viale Roma, 365, 54100, Massa (MS)</p></div></div><div class="flex flex-col justify-center items-center gap-2"><div class="flex justify-center items-center h-60 w-60 bg-gray rounded-xl transition-all duration-200 outline-none outline-0 outline-offset-0 hover:outline hover:outline-4 hover:outline-yellow hover:outline-offset-4 cursor-pointer"><img${ssrRenderAttr("src", _imports_1)} alt="" class="bg-center bg-contain bg-no-repeat h-52 w-52"></div><div class="flex flex-col justify-center items-center"><div class="flex items-center justify-center gap-1"><p class="font-bold">Panificio Drago</p><img${ssrRenderAttr("src", _imports_2)} alt="star" class="h-6 w-6"></div><p class="text-xs opacity-80">Viale Roma, 365, 54100, Massa (MS)</p></div></div></div></div><div class="max-w-screen-xl mx-auto flex flex-col justify-center items-center py-16 gap-12"><h2 class="text-4xl font-bold">IL TUO CALENDARIO DELLE MERENDE</h2></div></div>`);
}
const _sfc_setup = _sfc_main.setup;
_sfc_main.setup = (props, ctx) => {
  const ssrContext = useSSRContext();
  (ssrContext.modules || (ssrContext.modules = /* @__PURE__ */ new Set())).add("pages/index.vue");
  return _sfc_setup ? _sfc_setup(props, ctx) : void 0;
};
const index = /* @__PURE__ */ _export_sfc(_sfc_main, [["ssrRender", _sfc_ssrRender]]);

export { index as default };
//# sourceMappingURL=index-BboFMgWt.mjs.map
