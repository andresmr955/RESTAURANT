import { ApplicationConfig, provideBrowserGlobalErrorListeners, provideZonelessChangeDetection } from '@angular/core';
import { PreloadAllModules, provideRouter, withPreloading } from '@angular/router';
import { provideHttpClient, withInterceptors,  withFetch} from '@angular/common/http'; // ✅ importante
import { tokenInterceptor } from './core/interceptors/token-interceptor';

import { routes } from './app.routes';
import { provideClientHydration, withEventReplay } from '@angular/platform-browser';

export const appConfig: ApplicationConfig = {
  providers: [
    provideBrowserGlobalErrorListeners(),
    provideZonelessChangeDetection(),
    provideRouter(routes, withPreloading(PreloadAllModules)), 
    provideClientHydration(withEventReplay()),
    provideHttpClient( withFetch()),
    provideHttpClient(withInterceptors([tokenInterceptor]))
    // ... other providers
  ]
};
