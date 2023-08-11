#version 460 core

in vec3 posW;
in vec3 normW;
in vec2 texCoord;

layout(location = 0) out vec4 outputColor;

uniform vec3 gCamPos;

uniform vec3 gDiffuseLight;
uniform vec3 gSpecLight;
uniform vec3 gAmbientLight;
uniform float gSpecPower;
uniform float gLightInt;
uniform vec3 gLightAtt;
uniform vec3 gLightPos;

uniform sampler2D gDiffuseMap;
uniform vec3 gSpecMaterial;
uniform vec3 gAmbientMaterial;

void main() {
    vec3 normWFixed = normalize(normW);
    vec3 diffuseMaterial = texture(gDiffuseMap, texCoord).rgb;

    float distance = distance(gLightPos, posW);
    float att = gLightInt / (gLightAtt.x + gLightAtt.y * distance + gLightAtt.z * distance * distance);

    vec3 toLight = normalize(gLightPos - posW);
    float diffuseLight = max(dot(toLight, normWFixed), 0.0f);
    vec4 diffuseColor = vec4((diffuseMaterial * gDiffuseLight) * diffuseLight, 1.0f);

    vec3 toEye = normalize(gCamPos - posW);
    vec3 r = reflect(-toLight, normW);
    float t = pow(max(dot(r, toEye), 0.0f), gSpecPower);
    vec4 specColor = vec4((gSpecMaterial * gSpecLight) * t, 1.0f);

    vec4 ambientColor = vec4((diffuseMaterial * gAmbientMaterial) * gAmbientLight, 1.0f);

    outputColor = ((diffuseColor + specColor) * att) + ambientColor;
}
