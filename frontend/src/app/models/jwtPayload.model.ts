export interface JwtPayloadUser{
  user_id: number;
  username: string;
  email: string;
  is_manager: boolean;
  is_chef: boolean;
  is_cook: boolean;
  exp?: number;
  iat?: Number;
  jti?: string;
  token_type: string;
}