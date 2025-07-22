import { Injectable } from '@angular/core';
import { getCookie, setCookie, removeCookie } from 'typescript-cookie';
import { JwtPayload, jwtDecode} from "jwt-decode";



@Injectable({
  providedIn: 'root'
})
export class TokenService {
 constructor() { }

  saveToken(token: string) {
    setCookie('token-app', token, { expires: 365, path: '/' });
  }

  getToken() {
    const token = getCookie('token-app');
   
    return token;
  }

  removeToken() {
    removeCookie('token-app');
  }

  removeRefreshToken() {
    removeCookie('refresh-token-app');
  }

  saveRefreshToken(token: string) {
  
    setCookie('refresh-token-app', token, { expires: 365, path: '/' });
  }

  getRefreshToken() {
    const token = getCookie('refresh-token-app');
    return token;
  }

  isValidToken() {
    const token = this.getToken();
    if (!token) {
      return false;
    }
    const decodeToken = jwtDecode<JwtPayload>(token);
    if (decodeToken && decodeToken?.exp) {
      const tokenDate = new Date(0);
      console.log(tokenDate)
      tokenDate.setUTCSeconds(decodeToken.exp);
      const today = new Date();
      return tokenDate.getTime() > today.getTime();
    }
    return false;
  }

  isValidRefreshToken() {
    const token = this.getRefreshToken();
    if (!token) {
      return false;
    }
    const decodeToken = jwtDecode<JwtPayload>(token);
    if (decodeToken && decodeToken?.exp) {
      const tokenDate = new Date(0);
      tokenDate.setUTCSeconds(decodeToken.exp);
      const today = new Date();
      return tokenDate.getTime() > today.getTime();
    }
    return false;
  }
}