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
// Code original : crok_seamless Matchbox pour Autodesk Flame

// Adapted to Natron by F.Fernandez
// Original code : crok_seamless Matchbox for Autodesk Flame


// iChannel0: Front, filter=linear, wrap=repeat
// BBox: iChannel0

// The MIT License
// Copyright © 2017 Inigo Quilez
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction,
//including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
//subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
//THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
//IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
//OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


// One way to avoid texture tile repetition one using one small texture to cover a huge area.
// Based on Voronoise (https://www.shadertoy.com/view/Xd23Dh), a random offset is applied to
// the texture UVs per Voronoi cell. Distance to the cell is used to smooth the transitions
// between cells.
// It doesn't work with automatic mipmapping - one should compute derivatives by hand.

// based on https://www.shadertoy.com/view/4tsGzf



uniform float shuffle2 = 9.0; // Shuffle : ,min=0.0, max=10000
uniform float zoom2 = 3.0; // Detail : ,min=0.0001, max=10000
uniform float smoothness = 1.0; // Smoothness : ,min=0.0, max=2.0

vec2 resolution = vec2(iResolution.x, iResolution.y);


vec3 hash3( vec2 p ) { return fract(sin(vec3( dot(p,vec2(127.1,311.7)), dot(p,vec2(269.5,183.3)), dot(p,vec2(419.2,371.9)) ))*43758.5453); }

vec3 textureNoTile( in vec2 x, float v )
{
  x *= 10.0;
  vec2 p = floor(x);
  vec2 f = fract(x);

	float k = 1.0+63.0*pow(1.0-v,4.0);

	vec3 va = vec3(0.0);
	float wt = 0.0;
    for( int j=-2; j<=2; j++ )
    for( int i=-2; i<=2; i++ )
    {
      vec2 g = vec2( float(i),float(j) );
		  vec3 o = hash3( p + g );
      vec3 c = texture2D( iChannel0, .2*x + v*o.zy ).xyz;
      vec2 r = g - f + o.xy;
      float d = dot(r,r);
      float ww = 1.0 - smoothstep(0.0,2.0,dot(d,d));
      ww = pow( ww, 1.0 + 16.0*v * (2.0 - smoothness) );
      va += c*ww;
      wt += ww;
    }
    return va/wt;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
	vec2 uv = (fragCoord.xy / resolution.xy) - 0.5;

	vec3 col = textureNoTile(zoom2 * uv, shuffle2 * 0.1 ).xyz;

	fragColor = vec4( col, 1.0 );
}
