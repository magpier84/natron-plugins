//
//
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//                        MM.                          .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                     MM.  .MMMM        MMMMMMM    MMM.  .MM
//                    MM.  .MMM           MMMMMM     MMM.  .MM
//                   MM.  .MmM              MMMM      MMM.  .MM
//                  MM.  .MMM                 MM       MMM.  .MM
//                 MM.  .MMM                   M        MMM.  .MM
//                MM.  .MMM                              MMM.  .MM
//                 MM.  .MMM                            MMM.  .MM
//                  MM.  .MMM       M                  MMM.  .MM
//                   MM.  .MMM      MM                MMM.  .MM
//                    MM.  .MMM     MMM              MMM.  .MM
//                     MM.  .MMM    MMMM            MMM.  .MM
//                      MM.  .MMMMMMMMMMMMMMMMMMMMMMMM.  .MM
//                       MM.  .MMMMMMMMMMMMMMMMMMMMMM.  .MM
//                        MM.                          .MM
//                          MMMMMMMMMMMMMMMMMMMMMMMMMMMM
//
//
//
//
// Adaptation pour Natron par F. Fernandez
// Code original : crok_oil_paint Matchbox pour Autodesk Flame

// Adapted to Natron by F.Fernandez
// Original code : crok_oil_paint Matchbox for Autodesk Flame


// iChannel0: Source, filter=linear, wrap=mirror
// BBox: iChannel0


uniform int radius = 10; // Radius : ,min=0, max=100
uniform float velocity = 2.0; // Velocity : , min=0.0, max=100.0
uniform vec2 distortion = vec2(0.0,0.0); // Distorsion : 



float myGlobalTime = iTime*.05;

float rand(vec2 co){
	return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

float noise2f( in vec2 p )
{
	vec2 ip = vec2(floor(p));
	vec2 u = fract(p);
	u = u*u*(3.0-2.0*u);
	float res = mix(
		mix(rand(ip),  rand(ip+vec2(1.0,0.0)),u.x),
		mix(rand(ip+vec2(0.0,1.0)),   rand(ip+vec2(1.0,1.0)),u.x),
		u.y)
	;
	return res*res;
}

float fbm(vec2 c) {
	float f = 0.0;
	float w = 1.0;
	for (int i = 0; i < 8; i++) {
		f+= w*noise2f(c);
		c*=2.0;
		w*=0.5;
	}
	return f;
}

vec2 cMul(vec2 a, vec2 b) {
	return vec2( a.x*b.x -  a.y*b.y,a.x*b.y + a.y * b.x);
}

float pattern(  vec2 p, out vec2 q, out vec2 r )
{
	q.x = fbm( p  +0.00*myGlobalTime * velocity);
	q.y = fbm( p + vec2(1.0));
	
	r.x = fbm( p +1.0*q + vec2(distortion.x , distortion.y)+0.15*myGlobalTime * velocity );
	r.y = fbm( p+ 1.0*q + vec2(distortion.x, distortion.y)+0.126*myGlobalTime * velocity );
	return fbm(p +1.0*r + 0.0* myGlobalTime);
}

const vec3 color1 = vec3(0.101961,0.619608,0.666667);
const vec3 color2 = vec3(0.666667,0.666667,0.498039);
const vec3 color3 = vec3(0,0,0.164706);
const vec3 color4 = vec3(0.666667,1,1);

vec3 darken( vec3 s, vec3 d )
{
	return min(s,d);
}

vec3 multiply( vec3 s, vec3 d )
{
	return s*d;
}

vec3 colorBurn( vec3 s, vec3 d )
{
	return 1.0 - (1.0 - d) / s;
}

vec3 linearBurn( vec3 s, vec3 d )
{
	return s + d - 1.0;
}

vec3 darkerColor( vec3 s, vec3 d )
{
	return (s.x + s.y + s.z < d.x + d.y + d.z) ? s : d;
}

vec3 lighten( vec3 s, vec3 d )
{
	return max(s,d);
}

vec3 screen( vec3 s, vec3 d )
{
	return s + d - s * d;
}

vec3 colorDodge( vec3 s, vec3 d )
{
	return d / (1.0 - s);
}

vec3 linearDodge( vec3 s, vec3 d )
{
	return s + d;
}

vec3 lighterColor( vec3 s, vec3 d )
{
	return (s.x + s.y + s.z > d.x + d.y + d.z) ? s : d;
}

float overlay( float s, float d )
{
	return (d < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);
}

vec3 overlay( vec3 s, vec3 d )
{
	vec3 c;
	c.x = overlay(s.x,d.x);
	c.y = overlay(s.y,d.y);
	c.z = overlay(s.z,d.z);
	return c;
}

float softLight( float s, float d )
{
	return (s < 0.5) ? d - (1.0 - 2.0 * s) * d * (1.0 - d) 
		: (d < 0.25) ? d + (2.0 * s - 1.0) * d * ((16.0 * d - 12.0) * d + 3.0) 
					 : d + (2.0 * s - 1.0) * (sqrt(d) - d);
}

vec3 softLight( vec3 s, vec3 d )
{
	vec3 c;
	c.x = softLight(s.x,d.x);
	c.y = softLight(s.y,d.y);
	c.z = softLight(s.z,d.z);
	return c;
}

float hardLight( float s, float d )
{
	return (s < 0.5) ? 2.0 * s * d : 1.0 - 2.0 * (1.0 - s) * (1.0 - d);
}

vec3 hardLight( vec3 s, vec3 d )
{
	vec3 c;
	c.x = hardLight(s.x,d.x);
	c.y = hardLight(s.y,d.y);
	c.z = hardLight(s.z,d.z);
	return c;
}

float vividLight( float s, float d )
{
	return (s < 0.5) ? 1.0 - (1.0 - d) / (2.0 * s) : d / (2.0 * (1.0 - s));
}

vec3 vividLight( vec3 s, vec3 d )
{
	vec3 c;
	c.x = vividLight(s.x,d.x);
	c.y = vividLight(s.y,d.y);
	c.z = vividLight(s.z,d.z);
	return c;
}

vec3 linearLight( vec3 s, vec3 d )
{
	return 2.0 * s + d - 1.0;
}

float pinLight( float s, float d )
{
	return (2.0 * s - 1.0 > d) ? 2.0 * s - 1.0 : (s < 0.5 * d) ? 2.0 * s : d;
}

vec3 pinLight( vec3 s, vec3 d )
{
	vec3 c;
	c.x = pinLight(s.x,d.x);
	c.y = pinLight(s.y,d.y);
	c.z = pinLight(s.z,d.z);
	return c;
}

vec3 hardMix( vec3 s, vec3 d )
{
	return floor(s + d);
}

vec3 difference( vec3 s, vec3 d )
{
	return abs(d - s);
}

vec3 exclusion( vec3 s, vec3 d )
{
	return s + d - 2.0 * s * d;
}

vec3 subtract( vec3 s, vec3 d )
{
	return s - d;
}

vec3 divide( vec3 s, vec3 d )
{
	return s / d;
}

//	rgb<-->hsv functions by Sam Hocevar
//	http://lolengine.net/blog/2013/07/27/rgb-to-hsv-in-glsl
vec3 rgb2hsv(vec3 c)
{
	vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
	vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
	vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));
	
	float d = q.x - min(q.w, q.y);
	float e = 1.0e-10;
	return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
}

vec3 hsv2rgb(vec3 c)
{
	vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
	vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
	return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

vec3 hue( vec3 s, vec3 d )
{
	d = rgb2hsv(d);
	d.x = rgb2hsv(s).x;
	return hsv2rgb(d);
}

vec3 color( vec3 s, vec3 d )
{
	s = rgb2hsv(s);
	s.z = rgb2hsv(d).z;
	return hsv2rgb(s);
}

vec3 saturation( vec3 s, vec3 d )
{
	d = rgb2hsv(d);
	d.y = rgb2hsv(s).y;
	return hsv2rgb(d);
}

vec3 luminosity( vec3 s, vec3 d )
{
	float dLum = dot(d, vec3(0.3, 0.59, 0.11));
	float sLum = dot(s, vec3(0.3, 0.59, 0.11));
	float lum = sLum - dLum;
	vec3 c = d + lum;
	float minC = min(min(c.x, c.y), c.z);
	float maxC = max(max(c.x, c.y), c.z);
	if(minC < 0.0) return sLum + ((c - sLum) * sLum) / (sLum - minC);
	else if(maxC > 1.0) return sLum + ((c - sLum) * (1.0 - sLum)) / (maxC - sLum);
	else return c;
}
vec3 sample(const int x, const int y, vec2 delta, vec2 fragCoord)
{
	vec2 uv = (fragCoord.xy + vec2(x, y)) / iResolution.xy;
	uv = uv + delta;
	return texture2D(iChannel0, uv).xyz;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
 {
	 vec2 src_size = vec2 (1.0 / iResolution.x, 1.0 / iResolution.y);
     vec2 uv = fragCoord.xy/iResolution.xy;
     float n = float((radius + 1) * (radius + 1));
     int i; 
	 int j;
     vec3 m0 = vec3(0.0); vec3 m1 = vec3(0.0); vec3 m2 = vec3(0.0); vec3 m3 = vec3(0.0);
     vec3 s0 = vec3(0.0); vec3 s1 = vec3(0.0); vec3 s2 = vec3(0.0); vec3 s3 = vec3(0.0);
     vec3 c;

	 	 vec2 q;
	vec2 r;
	vec2 c3 = 1000.0*fragCoord.xy/ iResolution.xy;
	float f = pattern(c3*0.01,q,r);
	vec3 col = mix(color1,color2,clamp((f*f)*4.0,0.0,1.0));
	col = color2;
	col = mix(col,color3,clamp(length(q),0.0,1.0));
	col = mix(col,color4,clamp(length(r.x),0.0,1.0));
	
	vec3 col2 = (0.2*f*f*f+0.6*f*f+0.5*f)*col;
	vec2 delta =  col2.xy * 0.025;
	 
	const vec3 lumi = vec3(0.2126, 0.7152, 0.0722);
	
	vec3 hc =sample(-1,-1,delta,fragCoord) *  1.0 + sample( 0,-1,delta,fragCoord) *  2.0
		 	+sample( 1,-1,delta,fragCoord) *  1.0 + sample(-1, 1,delta,fragCoord) * -1.0
		 	+sample( 0, 1,delta,fragCoord) * -2.0 + sample( 1, 1,delta,fragCoord) * -1.0;
		
	vec3 vc =sample(-1,-1,delta,fragCoord) *  1.0 + sample(-1, 0,delta,fragCoord) *  2.0
		 	+sample(-1, 1,delta,fragCoord) *  1.0 + sample( 1,-1,delta,fragCoord) * -1.0
		 	+sample( 1, 0,delta,fragCoord) * -2.0 + sample( 1, 1,delta,fragCoord) * -1.0;
	
	vec3 c2 = sample(0, 0,delta,fragCoord);
	
	c2 -= pow(c2, vec3(0.2126, 0.7152, 0.0722)) * pow(dot(lumi, vc*vc + hc*hc), 0.5);
	

	uv = uv + delta; 
	 
     for (int j = -radius; j <= 0; ++j)  {
         for (int i = -radius; i <= 0; ++i)  {
             c = texture2D(iChannel0, uv + vec2(i,j) * src_size).rgb;
             m0 += c;
             s0 += c * c;
         }
     }

     for (int j = -radius; j <= 0; ++j)  {
         for (int i = 0; i <= radius; ++i)  {
             c = texture2D(iChannel0, uv + vec2(i,j) * src_size).rgb;
             m1 += c;
             s1 += c * c;
         }
     }

     for (int j = 0; j <= radius; ++j)  {
         for (int i = 0; i <= radius; ++i)  {
             c = texture2D(iChannel0, uv + vec2(i,j) * src_size).rgb;
             m2 += c;
             s2 += c * c;
         }
     }

     for (int j = 0; j <= radius; ++j)  {
         for (int i = -radius; i <= 0; ++i)  {
             c = texture2D(iChannel0, uv + vec2(i,j) * src_size).rgb;
             m3 += c;
             s3 += c * c;
         }
     }


	 vec4 result;
     float min_sigma2 = 1e+2;
     m0 /= n;
     s0 = abs(s0 / n - m0 * m0);

     float sigma2 = s0.r + s0.g + s0.b;
     if (sigma2 < min_sigma2) {
         min_sigma2 = sigma2;
         result = vec4(m0, 1.0);
     }

     m1 /= n;
     s1 = abs(s1 / n - m1 * m1);

     sigma2 = s1.r + s1.g + s1.b;
     if (sigma2 < min_sigma2) {
         min_sigma2 = sigma2;
         result = vec4(m1, 1.0);
     }

     m2 /= n;
     s2 = abs(s2 / n - m2 * m2);

     sigma2 = s2.r + s2.g + s2.b;
     if (sigma2 < min_sigma2) {
         min_sigma2 = sigma2;
         result = vec4(m2, 1.0);
     }

     m3 /= n;
     s3 = abs(s3 / n - m3 * m3);

     sigma2 = s3.r + s3.g + s3.b;
     if (sigma2 < min_sigma2) {
         min_sigma2 = sigma2;
         result = vec4(m3, 1.0);
     }
	

	vec4 res2 = vec4(overlay(screen( result.rgb,c2.rgb), result.rgb) , 1.0);
	vec3 col3 = texture2D(iChannel0, fragCoord.xy / iResolution.xy + col2.xy * 0.05 ).xyz;
	fragColor = vec4(saturation(col3,res2.rgb ),1.0);
	 

 }